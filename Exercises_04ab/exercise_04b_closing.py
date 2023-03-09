
import cv2
import sys
import numpy as np

#exercise_04a_opening value_i exercise_04a_input_01.pgm exercise_04a_output_01.pgm
if len(sys.argv) != 4:
    print('Start... ADD MORE COMMENTS BEFORE DELIVERY!!!')
    sys.exit(1)
else:
    try:
        img1 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)
        img2 = img1.copy()
        i = int(sys.argv[1])
        kernel = np.ones((2*i+1, 2*i+1), np.uint8)
        tmp = cv2.dilate(img2, kernel, iterations=1)
        closing = cv2.erode(tmp, kernel, iterations=1)

        cv2.imwrite(sys.argv[3], closing)
        cv2.imshow("Window: closing", closing)
        cv2.waitKey(0)

    except Exception as e:
        print(e)

    # exercise_04b_clo1_output.pgm is created:
    # python exercise_04b_closing.py 1 immed_gray_inv.pgm exercise_04b_clo1_output.pgm
    # exercise_04b_clo2_output.pgm is created:
    # python exercise_04b_closing.py 2 immed_gray_inv.pgm exercise_04b_clo2_output.pgm