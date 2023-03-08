"""
Exercise 02a. Implement a program 'exercise_02a_thresh' that thresholds
an input image exercise_02a_input_01.pgm at level 'value':

exercise_02a_thresh exercise_02a_input_01.pgm value exercise_02a_output_01.pgm

The thresholding operation is as follows: a pixel p will have
a value of 255 in exercise_02a_output_01.pgm if its value in
exercise_02a_input_01.pgm is greater or equal than that of
value; otherwise, p will have a value of 0.

The image 'cam_74_threshold100.pgm' is the result of thresholding
'cam_74.pgm' at value 100.
"""

import cv2 
import sys

#I made a copy of cam_74.pgm and renamed it to exercise_02a_input_01.pgm

if len(sys.argv) != 4:
    print('Invalid number of arguments. To run the code input "python <filename.py> <input_image> <value> <output_image>" Example: "python exercise_02a_thresh.py exercise_02a_input_01.pgm 100 exercise_02a_output_01.pgm"')
    sys.exit(1)
else:
    try:
        img1 = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
        value = int(sys.argv[2])
        row = img1.shape[0]
        column = img1.shape[1]
        img2 = img1.copy()

        for i in range(row):
            for j in range(column):
                value1 = img1[int(i), int(j)]
                if value1 >= value:
                    img2[int(i), int(j)] = 255
                else:
                    img2[int(i), int(j)] = value

        print("Saving image to file in folder")
        #The file called "Exercises_02ab\exercise_02a_output_01.pgm" that is in this folder is created by this code with a value at 100
        cv2.imwrite(sys.argv[3], img2)

        cv2.imshow("Window: img2", img2)
        cv2.waitKey(0)

    except Exception as e:
        print(e)