import math
import matplotlib.pyplot as plt

# Data: (Color Name, Wheel Position, (R, G, B))
color_data = [
    ("Red",     0,   (255,   0,   0)),
    ("Orange",  32,  (159,  96,   0)),
    ("Yellow",  64,  (63,  192,   0)),
    ("Green",   85,  (0,   255,   0)),
    ("Teal",   127,  (0,   129, 126)),
    ("Cyan",   128,  (0,   128, 127)),
    ("Blue",   170,  (0,     0, 255)),
    ("Purple", 191,  (63,    0, 192)),
    ("Magenta",213,  (126,   0, 129)),
    ("Pink",   234,  (189,   0,  66))
]

# Convert "wheel position" (0–255) to angle in radians on the circle
# We'll place each color on radius=1 for a straightforward color wheel.
def position_to_angle(pos):
    return (pos / 256.0) * 2.0 * math.pi

# Create a polar plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax.set_ylim(0, 1.3)  # Extend radius slightly for labels

# Draw a faint circle boundary (optional)
circle = plt.Circle((0,0), 1.0, transform=ax.transData._b, fill=False, linestyle='--')
ax.add_artist(circle)

# Plot each color and label
for name, wheel_pos, (r, g, b) in color_data:
    angle = position_to_angle(wheel_pos)
    
    # Normalize RGB to [0,1] for matplotlib
    color_rgb = (r/255.0, g/255.0, b/255.0)
    
    # Plot a small marker at radius=1
    ax.plot(angle, 1, marker='o', markersize=10, color=color_rgb)
    
    # Draw a radial line from the center to the point (a "callout")
    ax.plot([angle, angle], [0, 1], color="black", linewidth=0.5)
    
    # Place text just outside the circle (radius=1.1)
    label = f"{name}\nPos: {wheel_pos}\nRGB: {r}, {g}, {b}"
    ax.text(angle, 1.15, label,
            ha='center', va='center',
            fontsize=9)

# A bit of cleanup for the polar plot:
ax.set_theta_direction(-1)             # Make angles increase clockwise
ax.set_theta_offset(math.pi/2.0)       # Start 0 at the top (optional)
ax.set_xticks([])                      # Hide the default angular ticks
ax.set_yticks([])                      # Hide the radial ticks
ax.spines['polar'].set_visible(False)  # Hide the outer polar spine

plt.title("Technical Color Wheel Illustration", pad=20, fontsize=14)
plt.show()
