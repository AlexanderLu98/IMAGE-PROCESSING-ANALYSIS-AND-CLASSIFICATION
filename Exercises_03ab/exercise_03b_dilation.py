
import cv2
import sys
import numpy as np

#exercise_03b_dilation value_i exercise_03b_input_01.pgm exercise_03b_output_01.pgm
if len(sys.argv) != 4:
    print('python exercise_03b_dilation.py 1 immed_gray_inv.pgm exercise_03b_dil1_output.pgm')
    sys.exit(1)
else:
    try:
        img1 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)
        img2 = img1.copy()
        i = int(sys.argv[1])
        kernel = np.ones((2*i+1, 2*i+1), np.uint8)
        dilation = cv2.dilate(img2, kernel, iterations=1)


        cv2.imwrite(sys.argv[3], dilation)
        cv2.imshow("Window: img2", dilation)
        cv2.waitKey(0)

    except Exception as e:
        print(e)

    # exercise_03b_dil1_output.pgm is created:
    # python exercise_03b_dilation.py 1 immed_gray_inv.pgm exercise_03b_dil1_output.pgm
    # exercise_03b_dil2_output.pgm is created:
    # python exercise_03b_dilation.py 2 immed_gray_inv.pgm exercise_03b_dil2_output.pgm