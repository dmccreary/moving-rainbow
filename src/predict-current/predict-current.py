import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd

# Define the data points
data_points = [
    {"resistance": 4.6, "current": 150},
    {"resistance": 6.0, "current": 120},
    {"resistance": 9.9, "current": 75},
    {"resistance": 14.7, "current": 55},
    {"resistance": 20.9, "current": 32},
    {"resistance": 27.7, "current": 25},
    {"resistance": 31.0, "current": 20},
    {"resistance": 43, "current": 23},
    {"resistance": 92, "current": 13.3},
    {"resistance": 125, "current": 10.9},
    {"resistance": 151, "current": 8.7},
    {"resistance": 221, "current": 6.5},
    {"resistance": 330, "current": 5.9}
]

# Extract resistance and current values
resistance = np.array([point["resistance"] for point in data_points])
current = np.array([point["current"] for point in data_points])

# Reshape resistance for sklearn
X = resistance.reshape(-1, 1)
y = current

print("Original Data Points:")
print("Resistance (KΩ) | Current (mA)")
print("-" * 25)
for r, c in zip(resistance, current):
    print(f"{r:11.1f} | {c:10.1f}")
print()

# Try multiple regression approaches
results = {}

# 1. 2nd Order Polynomial
poly_features_2 = PolynomialFeatures(degree=2)
X_poly_2 = poly_features_2.fit_transform(X)
poly_reg_2 = LinearRegression()
poly_reg_2.fit(X_poly_2, y)
y_pred_2 = poly_reg_2.predict(X_poly_2)
r2_poly_2 = r2_score(y, y_pred_2)
results['2nd Order Polynomial'] = {
    'model': poly_reg_2,
    'features': poly_features_2,
    'r2': r2_poly_2,
    'pred': y_pred_2
}

# 2. 3rd Order Polynomial
poly_features_3 = PolynomialFeatures(degree=3)
X_poly_3 = poly_features_3.fit_transform(X)
poly_reg_3 = LinearRegression()
poly_reg_3.fit(X_poly_3, y)
y_pred_3 = poly_reg_3.predict(X_poly_3)
r2_poly_3 = r2_score(y, y_pred_3)
results['3rd Order Polynomial'] = {
    'model': poly_reg_3,
    'features': poly_features_3,
    'r2': r2_poly_3,
    'pred': y_pred_3
}

# 3. Inverse relationship (1/x)
X_inv = 1/X
inv_reg = LinearRegression()
inv_reg.fit(X_inv, y)
y_pred_inv = inv_reg.predict(X_inv)
r2_inv = r2_score(y, y_pred_inv)
results['Inverse (1/x)'] = {
    'model': inv_reg,
    'features': None,
    'r2': r2_inv,
    'pred': y_pred_inv
}

# Print R² values for comparison
print("Model Comparison (R² values):")
print("-" * 35)
for name, result in results.items():
    print(f"{name:20s}: {result['r2']:.6f}")
print()

# Find best model
best_model_name = max(results.keys(), key=lambda k: results[k]['r2'])
best_result = results[best_model_name]
print(f"Best fitting model: {best_model_name} (R² = {best_result['r2']:.6f})")
print()

# Print coefficients for each model
print("Model Equations:")
print("-" * 50)

# 2nd Order Polynomial
coeffs_2 = poly_reg_2.coef_
intercept_2 = poly_reg_2.intercept_
print(f"2nd Order: I = {coeffs_2[2]:.8f}R² + {coeffs_2[1]:.6f}R + {intercept_2:.6f}")

# 3rd Order Polynomial
coeffs_3 = poly_reg_3.coef_
intercept_3 = poly_reg_3.intercept_
print(f"3rd Order: I = {coeffs_3[3]:.10f}R³ + {coeffs_3[2]:.8f}R² + {coeffs_3[1]:.6f}R + {intercept_3:.6f}")

# Inverse relationship
inv_coeff = inv_reg.coef_[0]
inv_intercept = inv_reg.intercept_
print(f"Inverse:   I = {inv_coeff:.6f}/R + {inv_intercept:.6f}")
print()

# Generate smooth curves for plotting
resistance_smooth = np.linspace(4, 350, 200)
X_smooth = resistance_smooth.reshape(-1, 1)

# Calculate smooth predictions for each model
X_smooth_poly_2 = poly_features_2.transform(X_smooth)
current_smooth_2 = poly_reg_2.predict(X_smooth_poly_2)

X_smooth_poly_3 = poly_features_3.transform(X_smooth)
current_smooth_3 = poly_reg_3.predict(X_smooth_poly_3)

X_smooth_inv = 1/X_smooth
current_smooth_inv = inv_reg.predict(X_smooth_inv)

# Create the plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: Full range
ax1.scatter(resistance, current, color='red', s=100, label='Data Points', zorder=5)
ax1.plot(resistance_smooth, current_smooth_2, color='blue', linewidth=2, label=f'2nd Order (R²={r2_poly_2:.3f})')
ax1.plot(resistance_smooth, current_smooth_3, color='green', linewidth=2, label=f'3rd Order (R²={r2_poly_3:.3f})')
ax1.plot(resistance_smooth, current_smooth_inv, color='orange', linewidth=2, label=f'Inverse (R²={r2_inv:.3f})')
ax1.set_xlabel('Resistance (KΩ)')
ax1.set_ylabel('Current (mA)')
ax1.set_title('LED Current vs Resistance - Full Range')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_xlim(0, 350)
ax1.set_ylim(0, 160)

# Plot 2: Zoomed in (low resistance range)
resistance_zoom = np.linspace(4, 50, 100)
X_zoom = resistance_zoom.reshape(-1, 1)
X_zoom_poly_2 = poly_features_2.transform(X_zoom)
current_zoom_2 = poly_reg_2.predict(X_zoom_poly_2)
X_zoom_poly_3 = poly_features_3.transform(X_zoom)
current_zoom_3 = poly_reg_3.predict(X_zoom_poly_3)
X_zoom_inv = 1/X_zoom
current_zoom_inv = inv_reg.predict(X_zoom_inv)

# Filter data points for zoom
mask = resistance <= 50
ax2.scatter(resistance[mask], current[mask], color='red', s=100, label='Data Points', zorder=5)
ax2.plot(resistance_zoom, current_zoom_2, color='blue', linewidth=2, label=f'2nd Order (R²={r2_poly_2:.3f})')
ax2.plot(resistance_zoom, current_zoom_3, color='green', linewidth=2, label=f'3rd Order (R²={r2_poly_3:.3f})')
ax2.plot(resistance_zoom, current_zoom_inv, color='orange', linewidth=2, label=f'Inverse (R²={r2_inv:.3f})')
ax2.set_xlabel('Resistance (KΩ)')
ax2.set_ylabel('Current (mA)')
ax2.set_title('LED Current vs Resistance - Zoomed (0-50KΩ)')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_xlim(0, 50)
ax2.set_ylim(0, 160)

plt.tight_layout()
plt.show()

# Print JavaScript-ready coefficients for best model
print("For use in JavaScript (p5.js):")
print("-" * 40)

if best_model_name == '2nd Order Polynomial':
    print(f"// 2nd Order Polynomial: I = aR² + bR + c")
    print(f"let a = {coeffs_2[2]:.10f};  // coefficient of R²")
    print(f"let b = {coeffs_2[1]:.8f};   // coefficient of R")
    print(f"let c = {intercept_2:.8f};         // constant term")
    print("// predicted_current = a * resistance*resistance + b * resistance + c;")
elif best_model_name == '3rd Order Polynomial':
    print(f"// 3rd Order Polynomial: I = aR³ + bR² + cR + d")
    print(f"let a = {coeffs_3[3]:.12f}; // coefficient of R³")
    print(f"let b = {coeffs_3[2]:.10f}; // coefficient of R²")
    print(f"let c = {coeffs_3[1]:.8f};  // coefficient of R")
    print(f"let d = {intercept_3:.8f};        // constant term")
    print("// predicted_current = a*resistance*resistance*resistance + b*resistance*resistance + c*resistance + d;")
elif best_model_name == 'Inverse (1/x)':
    print(f"// Inverse relationship: I = a/R + b")
    print(f"let a = {inv_coeff:.8f};     // coefficient of 1/R")
    print(f"let b = {inv_intercept:.8f};        // constant term")
    print("// predicted_current = a / resistance + b;")
print()

# Test the best equation with original data points
print(f"Verification for {best_model_name}:")
print("Resistance | Actual | Predicted | Error")
print("-" * 40)

best_pred = best_result['pred']
for i, (r, actual, predicted) in enumerate(zip(resistance, current, best_pred)):
    error = abs(actual - predicted)
    print(f"{r:9.1f} | {actual:6.1f} | {predicted:9.1f} | {error:5.1f}")

# Calculate average error for best model
avg_error = np.mean(np.abs(current - best_pred))
print(f"\nAverage absolute error: {avg_error:.2f} mA")

# Suggest which model to use
print("\nRecommendation:")
print("-" * 40)
if r2_inv > 0.95:
    print("Use the INVERSE model (I = a/R + b) - it's simpler and fits well!")
    print("This makes physical sense for LED current vs resistance.")
elif r2_poly_3 > r2_poly_2 + 0.05:
    print("Use the 3rd ORDER POLYNOMIAL - significantly better fit than 2nd order.")
else:
    print("Use the 2nd ORDER POLYNOMIAL - good balance of simplicity and accuracy.")