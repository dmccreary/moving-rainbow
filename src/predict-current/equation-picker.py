import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit

# Define the data points - separating low and high resistance regions
all_data_points = [
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

# Split data at 30K ohms
low_resistance_data = [point for point in all_data_points if point["resistance"] <= 30]
high_resistance_data = [point for point in all_data_points if point["resistance"] > 30]

print("Data Analysis:")
print("=" * 50)
print(f"Low resistance points (≤30KΩ): {len(low_resistance_data)}")
print(f"High resistance points (>30KΩ): {len(high_resistance_data)}")
print()

# Extract low resistance values
resistance_low = np.array([point["resistance"] for point in low_resistance_data])
current_low = np.array([point["current"] for point in low_resistance_data])

print("Low Resistance Data (≤30KΩ):")
print("Resistance (KΩ) | Current (mA)")
print("-" * 25)
for r, c in zip(resistance_low, current_low):
    print(f"{r:11.1f} | {c:10.1f}")
print()

# Try multiple models for low resistance region
models = {}

# 1. Linear regression
X_low = resistance_low.reshape(-1, 1)
linear_reg = LinearRegression()
linear_reg.fit(X_low, current_low)
y_pred_linear = linear_reg.predict(X_low)
r2_linear = r2_score(current_low, y_pred_linear)
models['Linear'] = {
    'r2': r2_linear,
    'pred': y_pred_linear,
    'formula': f'I = {linear_reg.coef_[0]:.4f}R + {linear_reg.intercept_:.4f}'
}

# 2. 2nd order polynomial
poly_features_2 = PolynomialFeatures(degree=2)
X_poly_2 = poly_features_2.fit_transform(X_low)
poly_reg_2 = LinearRegression()
poly_reg_2.fit(X_poly_2, current_low)
y_pred_poly_2 = poly_reg_2.predict(X_poly_2)
r2_poly_2 = r2_score(current_low, y_pred_poly_2)
coeffs_2 = poly_reg_2.coef_
models['2nd Order Polynomial'] = {
    'r2': r2_poly_2,
    'pred': y_pred_poly_2,
    'formula': f'I = {coeffs_2[2]:.6f}R² + {coeffs_2[1]:.4f}R + {poly_reg_2.intercept_:.4f}'
}

# 3. 3rd order polynomial
poly_features_3 = PolynomialFeatures(degree=3)
X_poly_3 = poly_features_3.fit_transform(X_low)
poly_reg_3 = LinearRegression()
poly_reg_3.fit(X_poly_3, current_low)
y_pred_poly_3 = poly_reg_3.predict(X_poly_3)
r2_poly_3 = r2_score(current_low, y_pred_poly_3)
coeffs_3 = poly_reg_3.coef_
models['3rd Order Polynomial'] = {
    'r2': r2_poly_3,
    'pred': y_pred_poly_3,
    'formula': f'I = {coeffs_3[3]:.8f}R³ + {coeffs_3[2]:.6f}R² + {coeffs_3[1]:.4f}R + {poly_reg_3.intercept_:.4f}'
}

# 4. Exponential decay: I = a * exp(-b*R) + c
def exponential_decay(R, a, b, c):
    return a * np.exp(-b * R) + c

try:
    popt_exp, _ = curve_fit(exponential_decay, resistance_low, current_low, 
                           p0=[200, 0.1, 0], maxfev=5000)
    y_pred_exp = exponential_decay(resistance_low, *popt_exp)
    r2_exp = r2_score(current_low, y_pred_exp)
    models['Exponential Decay'] = {
        'r2': r2_exp,
        'pred': y_pred_exp,
        'formula': f'I = {popt_exp[0]:.4f} * exp(-{popt_exp[1]:.6f}R) + {popt_exp[2]:.4f}'
    }
except:
    print("Exponential fit failed")

# 5. Power law: I = a * R^(-b) + c
def power_law(R, a, b, c):
    return a * np.power(R, -b) + c

try:
    popt_power, _ = curve_fit(power_law, resistance_low, current_low, 
                             p0=[1000, 1, 0], maxfev=5000)
    y_pred_power = power_law(resistance_low, *popt_power)
    r2_power = r2_score(current_low, y_pred_power)
    models['Power Law'] = {
        'r2': r2_power,
        'pred': y_pred_power,
        'formula': f'I = {popt_power[0]:.4f} * R^(-{popt_power[1]:.6f}) + {popt_power[2]:.4f}'
    }
except:
    print("Power law fit failed")

# 6. Square root inverse: I = a / sqrt(R) + b
def sqrt_inverse(R, a, b):
    return a / np.sqrt(R) + b

try:
    popt_sqrt, _ = curve_fit(sqrt_inverse, resistance_low, current_low, 
                            p0=[500, 0], maxfev=5000)
    y_pred_sqrt = sqrt_inverse(resistance_low, *popt_sqrt)
    r2_sqrt = r2_score(current_low, y_pred_sqrt)
    models['Square Root Inverse'] = {
        'r2': r2_sqrt,
        'pred': y_pred_sqrt,
        'formula': f'I = {popt_sqrt[0]:.4f} / sqrt(R) + {popt_sqrt[1]:.4f}'
    }
except:
    print("Square root inverse fit failed")

# Print model comparison
print("Model Comparison for Low Resistance Region (≤30KΩ):")
print("=" * 60)
for name, model in sorted(models.items(), key=lambda x: x[1]['r2'], reverse=True):
    print(f"{name:20s}: R² = {model['r2']:.6f}")
    print(f"                     Formula: {model['formula']}")
    print()

# Find best model
best_model_name = max(models.keys(), key=lambda k: models[k]['r2'])
best_model = models[best_model_name]

print(f"BEST MODEL: {best_model_name}")
print(f"R² = {best_model['r2']:.6f}")
print(f"Formula: {best_model['formula']}")
print()

# Create visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: All models comparison
resistance_smooth = np.linspace(4, 32, 100)
colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown']

ax1.scatter(resistance_low, current_low, color='red', s=100, label='Data Points', zorder=5)

for i, (name, model) in enumerate(models.items()):
    if name == 'Linear':
        y_smooth = linear_reg.predict(resistance_smooth.reshape(-1, 1))
    elif name == '2nd Order Polynomial':
        X_smooth_poly = poly_features_2.transform(resistance_smooth.reshape(-1, 1))
        y_smooth = poly_reg_2.predict(X_smooth_poly)
    elif name == '3rd Order Polynomial':
        X_smooth_poly = poly_features_3.transform(resistance_smooth.reshape(-1, 1))
        y_smooth = poly_reg_3.predict(X_smooth_poly)
    elif name == 'Exponential Decay':
        y_smooth = exponential_decay(resistance_smooth, *popt_exp)
    elif name == 'Power Law':
        y_smooth = power_law(resistance_smooth, *popt_power)
    elif name == 'Square Root Inverse':
        y_smooth = sqrt_inverse(resistance_smooth, *popt_sqrt)
    
    ax1.plot(resistance_smooth, y_smooth, color=colors[i % len(colors)], 
             linewidth=2, label=f'{name} (R²={model["r2"]:.3f})')

ax1.set_xlabel('Resistance (KΩ)')
ax1.set_ylabel('Current (mA)')
ax1.set_title('Low Resistance Region: Model Comparison')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_xlim(4, 32)
ax1.set_ylim(0, 160)

# Plot 2: Best model detailed view
ax2.scatter(resistance_low, current_low, color='red', s=100, label='Data Points', zorder=5)

if best_model_name == 'Linear':
    y_smooth = linear_reg.predict(resistance_smooth.reshape(-1, 1))
elif best_model_name == '2nd Order Polynomial':
    X_smooth_poly = poly_features_2.transform(resistance_smooth.reshape(-1, 1))
    y_smooth = poly_reg_2.predict(X_smooth_poly)
elif best_model_name == '3rd Order Polynomial':
    X_smooth_poly = poly_features_3.transform(resistance_smooth.reshape(-1, 1))
    y_smooth = poly_reg_3.predict(X_smooth_poly)
elif best_model_name == 'Exponential Decay':
    y_smooth = exponential_decay(resistance_smooth, *popt_exp)
elif best_model_name == 'Power Law':
    y_smooth = power_law(resistance_smooth, *popt_power)
elif best_model_name == 'Square Root Inverse':
    y_smooth = sqrt_inverse(resistance_smooth, *popt_sqrt)

ax2.plot(resistance_smooth, y_smooth, color='blue', linewidth=3, label=f'Best Fit: {best_model_name}')
ax2.set_xlabel('Resistance (KΩ)')
ax2.set_ylabel('Current (mA)')
ax2.set_title(f'Best Model: {best_model_name}\nR² = {best_model["r2"]:.4f}')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_xlim(4, 32)
ax2.set_ylim(0, 160)

plt.tight_layout()
plt.show()

# Verification table
print("Verification for Best Model:")
print("Resistance | Actual | Predicted | Error")
print("-" * 40)
best_pred = best_model['pred']
for r, actual, predicted in zip(resistance_low, current_low, best_pred):
    error = abs(actual - predicted)
    print(f"{r:9.1f} | {actual:6.1f} | {predicted:9.1f} | {error:5.1f}")

avg_error = np.mean(np.abs(current_low - best_pred))
print(f"\nAverage absolute error: {avg_error:.2f} mA")

# JavaScript implementation suggestion
print("\n" + "="*60)
print("RECOMMENDED IMPLEMENTATION FOR P5.JS:")
print("="*60)

if best_model_name == 'Linear':
    print("// For resistance <= 30:")
    print(f"let slope_low = {linear_reg.coef_[0]:.6f};")
    print(f"let intercept_low = {linear_reg.intercept_:.6f};")
    print("// predicted_current = slope_low * resistance + intercept_low;")
    
elif best_model_name == '2nd Order Polynomial':
    print("// For resistance <= 30:")
    print(f"let a_low = {coeffs_2[2]:.8f};  // coefficient of R²")
    print(f"let b_low = {coeffs_2[1]:.6f};  // coefficient of R")
    print(f"let c_low = {poly_reg_2.intercept_:.6f};  // constant term")
    print("// predicted_current = a_low * resistance * resistance + b_low * resistance + c_low;")
    
elif best_model_name == '3rd Order Polynomial':
    print("// For resistance <= 30:")
    print(f"let a_low = {coeffs_3[3]:.10f}; // coefficient of R³")
    print(f"let b_low = {coeffs_3[2]:.8f};  // coefficient of R²")
    print(f"let c_low = {coeffs_3[1]:.6f};  // coefficient of R")
    print(f"let d_low = {poly_reg_3.intercept_:.6f};  // constant term")
    print("// predicted_current = a_low*resistance*resistance*resistance + b_low*resistance*resistance + c_low*resistance + d_low;")
    
elif best_model_name == 'Exponential Decay':
    print("// For resistance <= 30:")
    print(f"let a_low = {popt_exp[0]:.6f};  // amplitude")
    print(f"let b_low = {popt_exp[1]:.8f};  // decay rate")
    print(f"let c_low = {popt_exp[2]:.6f};  // offset")
    print("// predicted_current = a_low * Math.exp(-b_low * resistance) + c_low;")
    
elif best_model_name == 'Power Law':
    print("// For resistance <= 30:")
    print(f"let a_low = {popt_power[0]:.6f};  // amplitude")
    print(f"let b_low = {popt_power[1]:.8f};  // exponent")
    print(f"let c_low = {popt_power[2]:.6f};  // offset")
    print("// predicted_current = a_low * Math.pow(resistance, -b_low) + c_low;")
    
elif best_model_name == 'Square Root Inverse':
    print("// For resistance <= 30:")
    print(f"let a_low = {popt_sqrt[0]:.6f};  // amplitude")
    print(f"let b_low = {popt_sqrt[1]:.6f};  // offset")
    print("// predicted_current = a_low / Math.sqrt(resistance) + b_low;")

print("\n// For resistance > 30, use the inverse formula:")
print("let a_high = 1037.39195983;  // coefficient of 1/R")
print("let b_high = -9.73988157;    // constant term")
print("// predicted_current = a_high / resistance + b_high;")