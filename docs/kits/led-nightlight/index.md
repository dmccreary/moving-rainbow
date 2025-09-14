# LED Nightlight

## Calculating The Base-Limiting Resistor

|Resistor (K Ohms)|Current (milliamps)|
|---|---|
|4.6|150|
|6.0|120|
|9.9|75|
|20.9|32|
|27.7|25|
|31|20|

!!! prompt
    Please generate a new p5.js MicroSim using the standard-rules.md file as your guide.

    This MicroSim draws a chart with resistance on the X axis and current on the Y axis.
    This MicroSim has a single slider that allows the user to change the value of ancurrent limiting resistor.  It then will predict the current going through the LED.  Here are some of the points the chart we want you to display:

    |Resistor (K Ohms)|Current (milliamps)|
    |---|---|
    |4.6|150|
    |6.0|120|
    |9.9|75|
    |20.9|32|
    |27.7|25|
    |31|20|

    For the input slider, the resistence value must range from 3 to 50. 

    The microsim will display the points in the table above with small red dots but then have a blue line go through the points using a least-square-fit calculated slope and intercept.
    The chart should display the value of the resistor and the current.
    The chart should label the axis.

    The title is "LED Current for Base Limiting Resistor"