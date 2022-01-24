

# projection-experiment
Projection error can lead to rationale agents viewing the same object with contradicting observations.

For example, below is a cube containing four connected line segments- two blue and two red.\
        (Note: Created with projection-cube.py & cube.txt)

![plot](https://user-images.githubusercontent.com/84434778/150727426-2ba19867-9ff2-4e67-b802-29bce13c5ee3.png)

When viewed isometrically in 3D it is clear that the length of the blue line equals the length of the red line.

However, Observers X, Y, and Z (viewing the object along the respective axis at a far away distance) would each answer the following question differently:

Question: "Which line is longer; red or blue?"

Observer X: "Blue."\
Observer Y: "Red."\
Observer Z: "They are the same length."

Each of these observations represent three different kinds of wrong:

Observers X and Y have provided wrong answers.\
Observer Z has provided the right answer - however, for the wrong reason. This is revealed by a follow-on question:

Question: "What is the length of each line, if the shortest continuous element is length 1?"

Observer X: "Blue is \sqrt{2} and red is ."\
Observer Y: "Red."\
Observer Z: "They are the same length."
