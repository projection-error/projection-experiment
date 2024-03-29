
# Overview
This project explores the following problem:
- Embed two line segments, blue and red, in a 3-D cube.
- Analyze the apparent length of each line from different vantage points.
- Find the loci of vantage points where lines *appear* to have the same length.
        - **cube.txt** and **lines.txt** embed geometric coordinates
        - **projection-cube.py** plots the lines and cube in matplotlib
        - **projection-experiment.py** computes the apparent lengths from different vantages points and makes plots. 

# projection-experiment
Projection error can lead to rational agents viewing the same object and drawing contradicting observations.

For example, below is a cube containing four connected line segments- two blue and two red.\
        (Note: Created with projection-cube.py, cube.txt, and lines.txt)

![plot](https://user-images.githubusercontent.com/84434778/150727426-2ba19867-9ff2-4e67-b802-29bce13c5ee3.png)

When viewed isometrically in 3D it is clear that the length of the blue line equals the length of the red line.

However, Observers X, Y, and Z (viewing the object along the respective axis at a far away distance) would each answer the following question differently:

Question: "Which line is longer; red or blue?"

Observer X: "Red."\
![X](https://user-images.githubusercontent.com/84434778/150860407-ed9bb40a-1bad-4dfe-8430-40a5b738db2a.png)

Observer Y: "Blue."\
![Y](https://user-images.githubusercontent.com/84434778/150861176-90c68af3-596b-4ea4-84a7-62d0296fa359.png)

Observer Z: "They are the same length."\
![Z](https://user-images.githubusercontent.com/84434778/150860428-8c6e2801-5143-422d-abbc-87fc586ba8e8.png)



Each of these observations represent three different kinds of wrong:

Observers X and Y have provided wrong answers, with over-estimations and under-estimations for each line, respectively.\
Observer Z has provided the right answer - however, for the wrong reason! This is revealed by a follow-on question:

Question: "What is the length of each line, if the shortest continuous element is length 1?"

Observer X: "Blue is 2^0.5 and red is 2."\
Observer Y: "Red is 2 and blue is 2^0.5."\
Observer Z: "Blue is 2 and red is 2."

We know, however, that the true lengths are both 1 +2^0.5

I created this object as a description for how intelligent people can perceive a problem and, with perfect rationality, end up with differing perspectives. However, through the integration of all three viewpoints, it becomes possible to discover the true invariance of the situation. Once discovered, the problem is fully solved.

This example illustrates the perception of an object in 3D from 3 vantage points. Could there be other insights from other vantage points?

The green points shown in the following illustration represent locations from which the object is viewed and apparent lengths calculated.

![plot](https://user-images.githubusercontent.com/84434778/150730433-a48df29e-94bb-4f11-b026-ffc93da86018.png)

Using a colormap, it's possible to see how the perception of the blue lines changes depending on the viewing angle (darker blue is a longer line, while whiter is a shorter line).

![blue sphere](https://user-images.githubusercontent.com/84434778/150730553-7b43d36c-63fb-4a03-935f-a8a07fa6bb83.png)


The distribution is mirrored for the red line projections.

![red sphere](https://user-images.githubusercontent.com/84434778/150730559-170e8938-3f7f-43d6-a174-870a4baa20d7.png)

Finally, the mismatch between red and blue line lengths is computed and a colorscale used. This plot is pretty neat - it shows the planes of symmetry. Orbitting about either of these two planes continuously changes the lengths of both lines - but the apparent lengths remain equal!


<img src="https://user-images.githubusercontent.com/84434778/150727426-2ba19867-9ff2-4e67-b802-29bce13c5ee3.png" width="400" height="400"><img src="https://user-images.githubusercontent.com/84434778/150730619-d0bbb1d6-cd04-45c3-8abd-c871396917b3.png" width="400" height="400">





