#!/usr/bin/env python3
"""
Gmail Notifier - Blinks F7 key red when there are unread emails.

Setup required:
1. Enable IMAP in Gmail: Settings > See all settings > Forwarding and POP/IMAP > Enable IMAP
2. Create an App Password: Google Account > Security > 2-Step Verification > App passwords
3. Set environment variables:
   export GMAIL_USER="your.email@gmail.com"
   export GMAIL_APP_PASSWORD="your-16-char-app-password"

Or create ~/.gmail-notifier.conf with:
   GMAIL_USER=your.email@gmail.com
   GMAIL_APP_PASSWORD=your-16-char-app-password
"""
from RPiKeyboardConfig import RPiKeyboardConfig
import colorsys
import imaplib
import os
import time

def rgb_to_hsv(r, g, b):
    """Convert RGB (0-255) to HSV (0-255 scale for all components)."""
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    return (int(h * 255), int(s * 255), int(v * 255))

# F7 key matrix position
F7_KEY = [0, 7]

# Colors
RED = rgb_to_hsv(255, 0, 0)
OFF = (0, 0, 0)

# Check interval in seconds
CHECK_INTERVAL = 60

# Blink timing
BLINK_ON_TIME = 0.5
BLINK_OFF_TIME = 0.5

def load_credentials():
    """Load Gmail credentials from environment or config file."""
    user = os.environ.get('GMAIL_USER')
    password = os.environ.get('GMAIL_APP_PASSWORD')

    # Try config file if env vars not set
    if not user or not password:
        config_file = os.path.expanduser('~/.gmail-notifier.conf')
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and '=' in line and not line.startswith('#'):
                        key, value = line.split('=', 1)
                        if key == 'GMAIL_USER':
                            user = value
                        elif key == 'GMAIL_APP_PASSWORD':
                            password = value

    if not user or not password:
        raise ValueError(
            "Gmail credentials not found. Set GMAIL_USER and GMAIL_APP_PASSWORD "
            "environment variables or create ~/.gmail-notifier.conf"
        )

    return user, password

def get_unread_count(user, password):
    """Connect to Gmail and return unread email count."""
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(user, password)
        mail.select('INBOX')

        # Search for unread emails
        status, messages = mail.search(None, 'UNSEEN')

        if status == 'OK':
            unread_ids = messages[0].split()
            count = len(unread_ids)
        else:
            count = 0

        mail.logout()
        return count
    except Exception as e:
        print(f"Error checking Gmail: {e}")
        return -1  # Return -1 to indicate error

def main():
    # Load credentials first
    try:
        user, password = load_credentials()
        print(f"Using Gmail account: {user}")
    except ValueError as e:
        print(e)
        return

    keyboard = RPiKeyboardConfig()

    try:
        # Save current preset to restore later
        current_preset = keyboard.get_current_preset_index()

        # Enable direct LED control
        keyboard.set_led_direct_effect()

        print("Gmail Notifier running. Press Ctrl+C to stop.")
        print(f"Checking every {CHECK_INTERVAL} seconds...")

        last_check = 0
        unread_count = 0
        blink_state = False

        while True:
            current_time = time.time()

            # Check for new emails periodically
            if current_time - last_check >= CHECK_INTERVAL:
                new_count = get_unread_count(user, password)
                if new_count >= 0:  # Only update if no error
                    unread_count = new_count
                    if unread_count > 0:
                        print(f"You have {unread_count} unread email(s)")
                    else:
                        print("No unread emails")
                last_check = current_time

            # Blink F7 if there are unread emails
            if unread_count > 0:
                if blink_state:
                    keyboard.set_led_by_matrix(matrix=F7_KEY, colour=RED)
                else:
                    keyboard.set_led_by_matrix(matrix=F7_KEY, colour=OFF)
                keyboard.send_leds()
                blink_state = not blink_state
                time.sleep(BLINK_ON_TIME if blink_state else BLINK_OFF_TIME)
            else:
                # No unread emails - ensure F7 is off
                keyboard.set_led_by_matrix(matrix=F7_KEY, colour=OFF)
                keyboard.send_leds()
                time.sleep(1)  # Sleep longer when no notifications

    except KeyboardInterrupt:
        print("\nInterrupted by user")
    finally:
        # Cleanup: restore previous state
        keyboard.rgb_clear()
        keyboard.send_leds()
        keyboard.set_current_preset_index(current_preset, save_index=False)
        keyboard.close()

if __name__ == "__main__":
    main()
