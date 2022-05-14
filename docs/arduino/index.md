St. Patrick's Day Colors
=======
Patterns for St. Patricks Day

Here are some of the patterns:

* Fade in green on each pixel
* Turn random pixels on green or orange.
* A single green pixel moves from start to finish
* Cross runner - one green goes from start to end while a orange goes end to start
* All green
* First Half green followed by second half Orange
* Build of Quarter Green/Quarter Orange/Third quarter green/Last Quarter Orange
* Theater Chase in green

```
    fadeIn(1);
    randomOn(50);
    singleRunner();
    crossRunner();
    allGreen();
    halfGreenOrange();
    quarterGreenOrange();
    theaterChase(strip.Color(0, 255, 0), delayTime);
```