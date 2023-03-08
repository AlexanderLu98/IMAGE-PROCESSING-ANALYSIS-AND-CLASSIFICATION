
import cv2
import sys
import numpy as np

#exercise_03a_erosion value_i exercise_03a_input_01.pgm exercise_03a_output_01.pgm
if len(sys.argv) != 4:
    print('Start... ADD MORE COMMENTS BEFORE DELIVERY!!!')
    sys.exit(1)
else:
    try:
        img1 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)
        img2 = img1.copy()
        i = int(sys.argv[1])
        kernel = np.ones((2*i+1, 2*i+1), np.uint8)
        erosion = cv2.erode(img2, kernel, iterations=1)


        cv2.imwrite(sys.argv[3], erosion)
        cv2.imshow("Window: img2", erosion)
        cv2.waitKey(0)

    except Exception as e:
        print(e)

    # exercise_03a_ero1_output.pgm is created:
    # python exercise_03a_erosion3.py 1 immed_gray_inv.pgm exercise_03a_ero1_output.pgm
    # exercise_03a_ero2_output.pgm is created:
    # python exercise_03a_erosion3.py 2 immed_gray_inv.pgm exercise_03a_ero2_output.pgm