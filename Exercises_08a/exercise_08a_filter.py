import sys
import cv2
import numpy as np

if len(sys.argv) != 6:
    print('Example: python exercise_08a_filter.py isn_256.pgm filter_1_opening.pgm filter_2_closing.pgm filter_3_ope_clo.pgm filter_4_clo_ope.pgm')
    sys.exit(1)

else:

    try:
        img1 = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
        img2 = img1.copy()

        b = np.ones((3, 3), np.uint8)
        filter_1_opening = cv2.morphologyEx(img2, cv2.MORPH_OPEN, b)
        filter_2_closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, b)

        filter_3_ope_clo = cv2.morphologyEx(filter_2_closing, cv2.MORPH_OPEN, b)

        filter_4_clo_ope = cv2.morphologyEx(filter_1_opening, cv2.MORPH_CLOSE, b)

        cv2.imwrite(sys.argv[2], filter_1_opening)
        cv2.imwrite(sys.argv[3], filter_2_closing)
        cv2.imwrite(sys.argv[4], filter_3_ope_clo)
        cv2.imwrite(sys.argv[5], filter_4_clo_ope)

        cv2.imshow("Window: orginal", img1)
        cv2.imshow("Window: filter1", filter_1_opening)
        cv2.imshow("Window: filter2", filter_2_closing)
        cv2.imshow("Window: filter3", filter_3_ope_clo)
        cv2.imshow("Window: filter4", filter_4_clo_ope)
        cv2.waitKey(0)


    except Exception as e:
        print(e)

    #all the files is created by following line. exercise_08a_output_01.txt is written by me.
    #python exercise_08a_filter.py isn_256.pgm filter_1_opening.pgm filter_2_closing.pgm filter_3_ope_clo.pgm filter_4_clo_ope.pgm
