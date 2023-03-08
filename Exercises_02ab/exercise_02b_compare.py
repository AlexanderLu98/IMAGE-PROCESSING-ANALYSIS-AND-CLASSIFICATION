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
import cv2
import sys

if len(sys.argv) != 4:
    print('<exercise_02b_compare.py> <exercise_02b_input_01.pgm> <exercise_02b_input_02.pgm> <textfile>')
    sys.exit(1)
else:
    try:
        img1 = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)

        rows_img1 = img1.shape[0]
        columns_img1 = img1.shape[1]
        rows_img2 = img2.shape[0]
        columns_img2 = img2.shape[1]

        img1_values = []
        img2_values = []
        for i in range(rows_img1):
            for j in range(columns_img1):
                value = img1[int(i), int(j)]
                img1_values.append(value)

        for i in range(rows_img2):
            for j in range(columns_img2):
                value2 = img2[int(i), int(j)]
                img2_values.append(value2)

        #can also have a set place to write to
        f = open(sys.argv[3], "w")
        if img1_values == img2_values:
            f.write("1")
        else:
            f.write("0")
        f.close()

    except Exception as e:
        print(e)


#textfile compare_1 is created by the input: "python exercise_02b_compare.py cam_74.pgm cam_74.pgm compare_1.txt"
#textfile compare_0 is created by the input: "python exercise_02b_compare.py cam_74.pgm cam_74_threshold100.pgm compare_0.txt"