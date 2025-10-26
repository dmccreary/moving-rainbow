---
title: Battery Life Calculator
description: Calculate estimated battery life for LED noodle costumes based on number of noodles, brightness level, and battery type.
---

# Battery Life Calculator MicroSim

<iframe src="./main.html" width="100%" height="602" style="border:1px solid silver;"></iframe>

[Fullscreen](./main.html){ .md-button .md-button--primary target="_blank" }
[Edit](https://editor.p5js.org/dmccreary/sketches/rgqrj3D3y)
## Description

This interactive simulation helps students estimate how long LED costume components will operate on various battery types. By adjusting the number of LED noodles, brightness level, and battery type, students can see real-time calculations of battery capacity, current draw, and estimated runtime.

## Learning Objectives

Students will be able to:

1. **Apply** the battery life formula: Battery Life (hours) = Battery Capacity (mAh) ÷ Total Current Draw (mA)
2. **Analyze** how different variables affect battery runtime
3. **Evaluate** appropriate battery choices for different costume designs
4. **Compare** the trade-offs between brightness, number of LEDs, and battery life

## Key Concepts

### Battery Capacity (mAh)
Battery capacity is measured in milliamp-hours (mAh). Different battery types have different capacities:

- **AA Batteries**: 2,000-3,000 mAh each (can be combined in series or parallel)
- **9V Batteries**: 500-600 mAh
- **USB Power Packs**: 5,000-20,000+ mAh (variable by size)

### Current Draw
Each LED noodle consumes up to 100 milliamps (mA) at full brightness. The total current draw is:

**Total Current (mA) = Number of Noodles × Current per Noodle × Brightness Factor**

### Brightness Factor
Reducing brightness proportionally reduces current consumption. Running LEDs at 50% brightness uses approximately 50% of the maximum current.

## Lesson Plan

### Exploration Activity (10 minutes)

1. **Predict**: Ask students to predict which factors will have the greatest impact on battery life
2. **Explore**: Have students adjust each slider and observe the changes
3. **Record**: Students note the battery life for these scenarios:
   - 5 noodles at 100% brightness with a 9V battery
   - 5 noodles at 50% brightness with a 9V battery
   - 10 noodles at 50% brightness with a small USB power pack

### Guided Practice (15 minutes)

1. **Problem**: A student wants their costume to last 4 hours for a parade. They have 8 LED noodles.
   - What battery should they choose?
   - What brightness level do they need?
   - What are their options?

2. **Design Challenge**: Find three different combinations of battery type and brightness that will provide at least 3 hours of runtime with 6 noodles.

### Real-World Application

Discuss with students:

- Why might you choose lower brightness instead of a bigger battery?
- What are the trade-offs between cost, weight, and runtime?
- How do temperature and battery quality affect actual performance?
- Why is it good to have more battery life than you think you need?

## Assessment Questions

1. If doubling the number of LED noodles, what happens to battery life? (Answer: It is cut in half)
2. If a 9V battery lasts 1.1 hours with 5 noodles at 100% brightness, how long will it last at 50% brightness? (Answer: approximately 2.2 hours)
3. Why might the actual battery life differ from the calculated estimate? (Answer: Battery quality, temperature, efficiency variations, battery degradation)

## Extensions

- Calculate the cost per hour of runtime for different battery types
- Research rechargeable battery options and compare lifetime costs
- Design a complete costume power system with multiple components
- Investigate power-saving techniques like dimming or blinking patterns

## Technical Notes

- Maximum current per noodle: 100 mA
- Formula assumes linear relationship between brightness and current draw
- Real-world results may vary ±20% based on conditions
- Battery capacity decreases with higher discharge rates
