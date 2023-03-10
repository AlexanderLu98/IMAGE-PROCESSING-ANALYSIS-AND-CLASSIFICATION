"""
Exercise 02c. Implement a program 'exercise_02c_sup' that computes
the sup (supremum) of two input PGM images (arguments of the program).
The names of the executable and of the input images are indicated in the
following example call:

exercise_02c_sup exercise_02c_input_01.pgm exercise_02c_input_02.pgm exercise_02c_output_01.pgm

Analogous, implement a program 'exercise_02c_inf' for the inf (infimum) operation:
exercise_02c_inf exercise_02c_input_01.pgm exercise_02c_input_02.pgm exercise_02c_output_01.pgm

Example images:
 image1.pgm
 image2.pgm
 image1_sup_image2.pgm : sup of image1.pgm and image2.pgm
 image1_inf_image2.pgm : inf of image1.pgm and image2.pgm
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
"""

import cv2
import sys
import numpy as np


if len(sys.argv) != 4:
    print('Example: python exercise_02c_inf.py image1.pgm image2.pgm exercise_02c_inf_output_01.pgm')
    sys.exit(1)
else:
    try:
        img1 = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)

        result = np.minimum(img1, img2)

        cv2.imwrite(sys.argv[3], result)

        print("Saving image to file in folder")

        cv2.imshow("Window: result", result)
        cv2.waitKey(0)

    except Exception as e:
        print(e)

#python exercise_02c_inf.py image1.pgm image2.pgm exercise_02c_inf_output_01.pgm