
import cv2
import sys
import numpy as np

if len(sys.argv) != 4:
    print('example: python exercise_04a_opening.py 1 immed_gray_inv.pgm exercise_04a_ope1_output.pgm')
    sys.exit(1)
else:
    try:
        img1 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)
        img2 = img1.copy()
        i = int(sys.argv[1])
        kernel = np.ones((2*i+1, 2*i+1), np.uint8)
        tmp = cv2.erode(img2, kernel, iterations=1)
        opening = cv2.dilate(tmp, kernel, iterations=1)

        cv2.imwrite(sys.argv[3], opening)
        cv2.imshow("Window: opening", opening)
        cv2.waitKey(0)

    except Exception as e:
        print(e)

    # exercise_04a_ope1_output.pgm is created:
    # python exercise_04a_opening.py 1 immed_gray_inv.pgm exercise_04a_ope1_output.pgm
    # exercise_04a_ope2_output.pgm is created:
    # python exercise_04a_opening.py 2 immed_gray_inv.pgm exercise_04a_ope2_output.pgm