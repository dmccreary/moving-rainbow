# Calculating LED Noodle Battery Life

![](./necklace-at-party.png)

So your LED costume is the hit of your Halloween party.
But will your costume work all night?  This lab
and the attach MicroSim will help you find out!

## Introduction

In this lesson, students will learn how to calculate the battery life of their Halloween costumes that use LED Noodles. Understanding battery capacity and power consumption is essential for ensuring that costumes stay illuminated throughout Halloween festivities.

## Objectives

By the end of this lesson, students will be able to:

-   Understand the concept of milliamp hours (mAh) and how it relates to battery capacity.
-   Calculate the total current draw of their LED Noodle costumes.
-   Determine the estimated battery life based on different battery types and configurations.
-   Make informed decisions about battery choices for their costumes.

## Materials Needed

-   LED Noodles (1 to 5 per student)
-   Dimmer knobs
-   Various batteries (2, 3, or 4 AA batteries, 9-volt batteries, USB power packs)
-   Calculators
-   Worksheets for practice problems
-   Whiteboard and markers

## Background Knowledge

Students should have a basic understanding of:

-   Electrical current (measured in amperes or milliamperes)
-   Basic arithmetic operations

## Lesson Steps

### Step 1: Introduction to Milliamp Hours (mAh)

-   **Explain**: Milliamp hours (mAh) measure a battery's energy capacity. It indicates how much current a battery can supply over one hour.
-   **Example**: A battery rated at 2000 mAh can deliver 2000 milliamps for one hour or 1000 milliamps for two hours.

### Step 2: Understanding Battery Capacities

-   **Discuss** the typical capacities of different batteries:

    -   **AA Batteries**: Approximately 2000--3000 mAh each
    -   **9-Volt Batteries**: Around 500--600 mAh
    -   **USB Power Packs**: Varies widely (e.g., 5000 mAh, 10000 mAh)
-   **Note**: Using multiple AA batteries in series increases voltage but not capacity. Parallel configurations increase capacity but are not typical for AA batteries in standard holders.

### Step 3: Calculating Total Current Draw

-   **Explain** how to determine the total current draw:

    -   **Per LED Noodle**: Up to 100 milliamps (mA) at full brightness
    -   **Dimmer Setting**: Adjusts brightness and reduces current draw proportionally
-   **Formula**:

```
**Total Current Draw (mA)** = Number of LED Noodles × Current per Noodle (mA) × Brightness Factor
```
**Brightness Factor**: Percentage of maximum brightness (e.g., 50% brightness = 0.5)

**Example**:

-   3 LED Noodles at 75% brightness:

        ```

        `Total Current Draw = 3 × 100 mA × 0.75 = 225 mA
        `

        ```

### Step 4: Calculating Battery Life

-   **Introduce** the formula for battery life:

    ```
    java
    Copy code

    `Battery Life (hours) = Battery Capacity (mAh) ÷ Total Current Draw (mA)
    `

    ```

-   **Considerations**:

    -   Real-world battery life may be less due to factors like battery age and efficiency.
    -   Battery capacity remains the same in series configurations but voltage increases.
-   **Example**:

    -   Using a USB power pack of 5000 mAh with a total current draw of 225 mA:

        ```
        java
        Copy code

        `Battery Life = 5000 mAh ÷ 225 mA ≈ 22.22 hours
        `

        ```

### Step 5: Practice Problems

-   **Provide** scenarios for students to calculate:

    1.  **Scenario**: A costume uses 5 LED Noodles at full brightness with a 9-volt battery (600 mAh).

        -   **Calculate Total Current Draw**:

            ```
            java
            Copy code

            `Total Current Draw = 5 × 100 mA × 1.0 = 500 mA
            `

            ```

        -   **Calculate Battery Life**:

            ```
            java
            Copy code

            `Battery Life = 600 mAh ÷ 500 mA = 1.2 hours
            `

            ```

    2.  **Scenario**: A student uses 2 AA batteries (total capacity of one AA battery is 2500 mAh) with 2 LED Noodles at 50% brightness.

        -   **Note**: Capacity remains 2500 mAh; voltage increases with batteries in series.

        -   **Calculate Total Current Draw**:

            ```
            java
            Copy code

            `Total Current Draw = 2 × 100 mA × 0.5 = 100 mA
            `

            ```

        -   **Calculate Battery Life**:

            ```
            java
            Copy code

            `Battery Life = 2500 mAh ÷ 100 mA = 25 hours
            `

            ```

### Step 6: Discuss Real-World Factors

-   **Explain** that actual battery life may vary due to:

    -   Battery quality and age
    -   Ambient temperature
    -   Variations in LED efficiency
-   **Encourage** students to consider these factors in their planning.

## Conclusion

-   **Recap** the importance of calculating battery life.
-   **Emphasize** making informed choices to ensure costumes remain illuminated.

## Assessment

-   **Worksheet Completion**: Collect and review practice problem worksheets.
-   **Group Discussion**: Share calculations and discuss any differences.

## Additional Resources

-   [Battery Life Calculator](#) *(Link to JavaScript-powered battery lifetime calculator)*

requestAnimationFrame((function(){window.\_\_oai\_logTTI?window.\_\_oai\_logTTI():window.\_\_oai\_SSR\_TTI=window.\_\_oai\_SSR\_TTI??Date.now()}))
 

## Sample ChatGPT Prompt

```linenums="0"
I am working with a class of 9th grade students that are
using LED Noodles that consume up to 100 milliamps when fully bright.
They are used in Halloween costumes.

We use a variety of power sources including 2, 3 or 4, AA batteries,
9-volt batteries and a variety of USB power packs.
The costumes have a dimmer know that allows the students to adjust the brightness of their costumes.  Their costumes have between one and five LED noodles.

Please generate a complete lesson plan that helps students
learn to calculate the battery life of our costumes based on milliamp hours.

Return the lesson plan in Markdown format with each section
using a level 2 header.
Assume at the end of the lesson there is a link to a JavaScript powered battery lifetime calculator.
```

Sample MicroSim Prompt

```linenums="0"
Create a p5.js sketch that simulates a LED noodle battery life calculator.
The title of the sketch is LED Noodle battery Life Calculator
The sketch as a series of input controls using a selection list and sliders.
The purpose of the calculator is to estimate how long an LED costume will last.
The  inputs to the calculator are the following:

1. Battery Type - (Selection List Values of: AA, AAA, 9-volt, USB Battery Pack (small, medium and large) - default AA
2. Number of batteries (Slider 1, 2, 3 or 4 batteries) - default 2
3. Number of LED noodle (Slider with values of 1, 2, 3, 4, or 5) - default 2
4. Current draw for each noodle (Slider with labeled values of (very dim, dim, medium, bright, very bright) with values of 2 milliamps, 5 milliamps, 10 milliamps, 50 milliamps, 100 milliamps)

As the user change the sliders, continually update the following:
Output Line 1: the total milliamp hours of the battery
Output Line 2:  the total current draw for the costume
Output Line 3:
The estimated time for the costume to reach 50% brightness due to battery drain
```