"""
Exercise 02b. Implement a program 'exercise_02b_compare' that compares two
input PGM images (arguments of the program). The names of the
executable and of the input images are indicated in the 
following example call:
exercise_02b_compare exercise_02b_input_01.pgm exercise_02b_input_02.pgm
The program should write '1' or '0' (without quotes) to an output
file called exercise_02b_output_01.txt depending on whether the
pgm images are equal or not.
The sizes of the input images could be different, in which case
exercise_02b_output_01.txt should contain '0' .
Note: two images I1 and I2 of identical sizes are equal if and only
if the intensity value of every pixel (x,y) of I1 is equal to
the intensity value of the same pixel (x,y) of I2.
Note: for checking, the previously mentioned images cam_74.pgm
and cam_74_threshold100.pgm could be used:
exercise_02b_compare cam_74.pgm cam_74.pgm
should give us that the images are equal.
On the other hand,
exercise_02b_compare cam_74.pgm cam_74_threshold100.pgm
should give us that the images are not equal.
"""