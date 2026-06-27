# Getting Around the macOS USB Bugs

macOS has had several USB device enumeration regressions that prevent
the Raspberry Pi Pico from connecting. This page documents the known
issues and the exact steps to work around them.

## Quick Diagnosis

Plug in your Pico and run:

```bash
ls /dev/cu.*
```

You should see a device like `/dev/cu.usbmodem14301`. If you only see
Bluetooth entries, the Pico is not being detected.

Next, check whether the Mac can see it at the USB hardware level:

```bash
ioreg -p IOUSB -l -w 0 | grep -E "idVendor|USB Product Name" | grep -v "Apple\|1452"
```

- **Nothing appears** → USB enumeration is completely blocked (see macOS 26 bug below).
- **"RP2 Boot" appears but no `/dev/cu.*`** → The device is seen but not mounted or
  the CDC serial driver is blocked (see the mounting workaround below).
- **A `usbmodem` entry appears** → The Pico is connected; check your IDE's port setting.

---

## macOS 26 (Tahoe) USB Enumeration Bug

### Symptoms

- Pico LED blinks (power is fine) but `ls /dev/cu.*` shows nothing.
- Even holding **BOOTSEL** while plugging in produces no `RPI-RP2` drive in Finder.
- `system_profiler SPUSBDataType` shows only internal Apple devices.
- The problem occurs on an Intel MacBook Pro. Other Macs nearby work fine.
- USB hubs with USB-A ports do **not** fix the problem.

### Root cause

macOS Tahoe 26.0 through 26.5 introduced a regression in the USB stack on Intel
Macs that prevents USB Full Speed (USB 1.1, 12 Mbps) devices from being enumerated.
The Pico operates at Full Speed, so it receives power but is never recognised as a
USB device. This is a kernel/OS-level block — no hub, adapter, or driver change
will work around it.

### Fix: update to macOS Tahoe 26.5.1

First, check your current version and what updates are available:

```bash
sw_vers
softwareupdate -l
```

If macOS Tahoe 26.5.1 is listed, install it. The GUI updater in
**System Settings → General → Software Update** is more reliable than
the command-line tool for large OS updates.

!!! warning "Stuck update daemon"
    If the update stalls indefinitely (no CPU or disk I/O for over 30 minutes),
    a stuck `UpdateBrainService` process from a previous update attempt may be
    blocking it. Check with:
    ```bash
    ps aux | grep UpdateBrain | grep -v grep
    ```
    If you see a process that started days or weeks ago, kill it with
    `sudo kill -9 <PID>`, then cancel the GUI update, do a normal restart
    (**Apple menu → Restart**), and try again with a clean boot.

---

## First Connection After Updating to 26.5.1

After updating, the Pico should enumerate. However, the first time you
connect in **BOOTSEL mode**, macOS may detect the device but not auto-mount
the `RPI-RP2` drive. If it does not appear in Finder:

```bash
diskutil list | grep RPI
```

If you see something like `/dev/disk2s1`, mount it manually:

```bash
diskutil mount disk2s1
```

The `RPI-RP2` drive will appear in Finder immediately.

---

## Flashing Firmware via the Command Line

Finder's drag-and-drop copy to `RPI-RP2` often hangs during the
"Preparing to copy" phase. This is because the Pico reboots the instant
it receives a valid UF2 file, and Finder panics when the volume disappears
mid-transfer.

Use `cp` in the terminal instead — it handles the disappearing volume cleanly:

```bash
cp ~/Desktop/RPI_PICO-20260406-v1.28.0.uf2 /Volumes/RPI-RP2/
```

The Pico will reboot immediately. `cp` may print an I/O error — that is
expected and harmless. Wait three seconds, then check for the serial port:

```bash
ls /dev/cu.*
```

You should see `/dev/cu.usbmodem*`. The Pico is ready.

---

## Checking the "Allow Accessories to Connect" Setting

macOS 13 (Ventura) and later added a privacy gate that controls whether
USB accessories are allowed to connect. In macOS 26 the search result for
"Allow accessories to connect" in System Settings may navigate to the wrong
section. Navigate there directly:

**System Settings → Privacy & Security → scroll to the bottom of the right pane**

Look for "Allow accessories to connect" and set it to
**Automatically when unlocked** or **Always** so the Pico is not blocked.

---

## Summary Table

| Symptom | Cause | Fix |
|---------|-------|-----|
| Pico invisible to Mac, even in BOOTSEL mode | macOS 26.0–26.5 USB regression | Update to macOS 26.5.1 |
| `RPI-RP2` detected but not mounted in Finder | USB accessory gate blocking auto-mount | `diskutil mount disk2s1` |
| Finder copy to `RPI-RP2` hangs at "Preparing" | Pico reboots mid-copy, confusing Finder | Use `cp` in Terminal |
| Serial port not appearing after firmware flash | CDC driver blocked or device not enumerated | Check `ioreg`, verify 26.5.1, check Privacy & Security |
| Update stalls indefinitely | Stuck `UpdateBrainService` process | Kill the process, restart Mac, retry update |
