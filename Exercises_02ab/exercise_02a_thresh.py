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

#img_path = input("Please write the path to your picture: ")
#Reads the picture file, can also implement the decesion to input the path to the chosen file
img1 = cv2.imread("Exercises_02ab\exercise_02a_input_01.pgm", cv2.IMREAD_GRAYSCALE)
row = img1.shape[0]
column = img1.shape[1]
img2 = img1.copy()

#Gives the oppurtunity to choose the value
value = int(input("Input value as an Integer: "))

for x in range(row):
    for y in range(column):
        value1 = img1[int(x), int(y)]
        if value1 >= value:
            img2[int(x), int(y)] = 255
        else:
            img2[int(x), int(y)] = value

#Saving the picture file, can also implement the decesion to input the path to the chosen file
print("Saving image to file exercise_02a_output_01.pgm ...")
#The file called "Exercises_02ab\exercise_02a_output_01.pgm" that is in this folder is created by this code with a value at 100
cv2.imwrite("Exercises_02ab\exercise_02a_output_01.pgm", img2)

cv2.imshow("Window: img2", img2)
cv2.waitKey(0) # waiting for a key