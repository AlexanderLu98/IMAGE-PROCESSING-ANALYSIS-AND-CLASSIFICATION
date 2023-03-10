
import cv2
import sys
import numpy as np

#exercise_04a_opening value_i exercise_04a_input_01.pgm exercise_04a_output_01.pgm
if len(sys.argv) != 4:
    print('Example: python exercise_06a_closing_opening.py 2 immed_gray_inv.pgm exercise_06a_clo2ope2_output.pgm')
    sys.exit(1)
else:
    try:
        img1 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)
        img2 = img1.copy()
        i = int(sys.argv[1])
        kernel = np.ones((2*i+1, 2*i+1), np.uint8)
        tmp = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)
        clo_ope = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)

        cv2.imwrite(sys.argv[3], clo_ope)
        cv2.imshow("Window: clo_ope", clo_ope)
        cv2.waitKey(0)

    except Exception as e:
        print(e)

    # exercise_06a_ope2clo2_output.pgm is created:
    # python exercise_06a_closing_opening.py 2 immed_gray_inv.pgm exercise_06a_clo2ope2_output.pgm
    # exercise_06a_ope4clo4_output.pgm is created:
    # python exercise_06a_closing_opening.py 4 immed_gray_inv.pgm exercise_06a_clo4ope4_output.pgm