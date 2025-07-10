import mediapipe as mp
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from landmarks_utilities import draw_eyes_landmarks, draw_nose_landmarks

def get_cordinates(img_path):
    """
        This function takes img_path as input and return two lists,
        Each list contains four cordinates(x,y) points named 1,2,3,4 that are basically the vertives of the rectangle formed by connecting all the points
        that basically embound eyes, and we will use this cordinates to slice the dataframe that contains temperature information corresponding to
        each pixels.
    """
    img = cv2.imread(img_path)
    left_list,right_list = draw_eyes_landmarks(img_path)
    # print(left_list)
    # print(right_list)
    left_x = []
    left_y = []
    right_x = []
    right_y = []

    for tup in left_list:
        left_x.append(tup[0])
        left_y.append(tup[1])

    for tup in right_list:
        right_x.append(tup[0])
        right_y.append(tup[1])

    min_left_x = min(left_x)
    max_left_x = max(left_x)
    min_left_y = min(left_y)
    max_left_y = max(left_y)

    min_right_x = min(right_x)
    max_right_x = max(right_x)
    min_right_y = min(right_y)
    max_right_y = max(right_y)

    diff_left_x = max_left_x - min_left_x
    diff_left_y = max_left_y - min_left_y

    p1_left = (min_left_x, min_left_y)
    p2_left = (min_left_x, max_left_y)
    p3_left = (max_left_x, min_left_y)
    p4_left = (max_left_x, max_left_y)

    p1_right = (min_right_x, min_right_y)
    p2_right = (min_right_x, max_right_y)
    p3_right = (max_right_x, min_right_y)
    p4_right = (max_right_x, max_right_y)

    cv2.circle(img, p1_left, 2, (0,255,0), -1)
    cv2.circle(img, p2_left, 2, (0,255,0), -1)
    cv2.circle(img, p3_left, 2, (0,255,0), -1)
    cv2.circle(img, p4_left, 2, (0,255,0), -1)

    cv2.circle(img, p1_right, 2, (0,255,0), -1)
    cv2.circle(img, p2_right, 2, (0,255,0), -1)
    cv2.circle(img, p3_right, 2, (0,255,0), -1)
    cv2.circle(img, p4_right, 2, (0,255,0), -1)



    cv2.imshow('my frame', img)
    cv2.waitKey()
    
    cordinates_left = [p1_left, p2_left, p3_left, p4_left]
    cordinates_right = [p1_right, p2_right, p3_right ,p4_right]

    return cordinates_left, cordinates_right



##########################################################
# img_path = "resized_image_Screenshot 2025-06-30 125137.png.jpg"

# l1, l2 = get_cordinates(img_path)
# print(l1)
# print(l2)

############################################################################

# img_path = "resized_image_Screenshot 2025-06-30 125137.png.jpg"

# img = cv2.imread(img_path)

# left_list,right_list = draw_eyes_landmarks(img_path)
# # print(left_list)
# # print(right_list)
# left_x = []
# left_y = []
# right_x = []
# right_y = []

# for tup in left_list:
#     left_x.append(tup[0])
#     left_y.append(tup[1])

# for tup in right_list:
#     right_x.append(tup[0])
#     right_y.append(tup[1])

# # print(left_x)
# # print(left_y)
# # print(right_x)
# # print(right_y)

# min_left_x = min(left_x)
# max_left_x = max(left_x)
# min_left_y = min(left_y)
# max_left_y = max(left_y)

# min_right_x = min(right_x)
# max_right_x = max(right_x)
# min_right_y = min(right_y)
# max_right_y = max(right_y)

# diff_left_x = max_left_x - min_left_x
# diff_left_y = max_left_y - min_left_y

# p1 = (min_left_x, min_left_y)
# p2 = (min_left_x, max_left_y)
# p3 = (max_left_x, min_left_y)
# p4 = (max_left_x, max_left_y)

# cv2.circle(img, p1, 2, (0,255,0), -1)
# cv2.circle(img, p2, 2, (0,255,0), -1)
# cv2.circle(img, p3, 2, (0,255,0), -1)
# cv2.circle(img, p4, 2, (0,255,0), -1)



# cv2.imshow('my frame', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

###############################