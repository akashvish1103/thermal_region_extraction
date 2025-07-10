import mediapipe as mp
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Function Definition

def draw_eyes_landmarks(img_path):
    """
        This function takes an image path, returns two list of tuples i.e. [(x1,y1), (x2,y2),....] 
        and display the iamge with highlited landmarks of both the eyes points 
        Both returned list contains the mediapipe eyes landmarks cordinate (x,y) for left_eye and right_eye
    """
    left_eye_indices = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
    right_eye_indices = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
    img = cv2.imread(img_path)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    height,width,_ = img.shape

    mp_face = mp.solutions.face_mesh
    face_mesh = mp_face.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5)
    # mp_draw = mp.solutions.drawing_utils

    results = face_mesh.process(rgb_img)
    left_list = []
    right_list = []
    for face_landmarks in results.multi_face_landmarks:
        for i in left_eye_indices:
            lm = face_landmarks.landmark[i]
            x = lm.x                          # This will be beteween 0 and 1
            y = lm.y
            x_normalized = x*width    
            y_normalized = y*height
            left_list.append((int(x_normalized), int(y_normalized)))

    for face_landmarks in results.multi_face_landmarks:
        for i in right_eye_indices:
            lm = face_landmarks.landmark[i]
            x = lm.x                          # This will be beteween 0 and 1
            y = lm.y
            x_normalized = x*width    
            y_normalized = y*height
            right_list.append((int(x_normalized), int(y_normalized)))


    # print(right_list)
    print(len(left_list))
    print(len(right_list))

    for tup in left_list:
        cv2.circle(img, (tup[0],tup[1]), 2, (0,255,0), -1)

    for tup in right_list:
        cv2.circle(img, (tup[0],tup[1]), 2, (0,255,0), -1)

    # cv2.imshow('my frame', img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    return left_list, right_list

###############################################################################################################################
# Function Definition nose

def draw_nose_landmarks(img_path):
    """
        This function an image path, returns ONE list of tuples i.e. [(x1,y1), (x2,y2),....]
        and display the iamge with highlited landmarks of nose points 
    """
    nose_indices = [1, 2, 4, 5, 6, 19, 94, 97, 98, 195, 197, 326, 327]

    img = cv2.imread(img_path)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    height,width,_ = img.shape

    mp_face = mp.solutions.face_mesh
    face_mesh = mp_face.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5)
    # mp_draw = mp.solutions.drawing_utils

    results = face_mesh.process(rgb_img)
    nose_list = []

    for face_landmarks in results.multi_face_landmarks:
        for i in nose_indices:
            lm = face_landmarks.landmark[i]
            x = lm.x                          # This will be beteween 0 and 1
            y = lm.y
            x_normalized = x*width    
            y_normalized = y*height
            nose_list.append((int(x_normalized), int(y_normalized)))


    # print(nose_list)
    print(len(nose_list))

    for tup in nose_list:
        cv2.circle(img, (tup[0],tup[1]), 2, (0,255,0), -1)

    # cv2.imshow('my frame', img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    return nose_list

##############################################################################################################################



# img_path = "resized_640x480.jpg"

# res1 = draw_eyes_landmarks(img_path)
# print(res1)

# res2 = draw_nose_landmarks(img_path)
# print(res2)

# img = cv2.imread(img_path)
# print(img.shape)

#######################################################


# LEFT_EYE_LANDMARKS = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
# RIGHT_EYE_LANDMARKS = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]


# img = cv2.imread("Screenshot 2025-06-30 125137.png")
# rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# height,width,_ = img.shape

# mp_face = mp.solutions.face_mesh
# face_mesh = mp_face.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5)
# mp_draw = mp.solutions.drawing_utils

# results = face_mesh.process(rgb_img)
# l = []
# for face_landmarks in results.multi_face_landmarks:
#     for i in LEFT_EYE_LANDMARKS:
#         lm = face_landmarks.landmark[i]
#         x = lm.x                          # This will be beteween 0 and 1
#         y = lm.y
#         x_normalized = x*width    
#         y_normalized = y*height
#         l.append((int(x_normalized), int(y_normalized)))

# print(l)
# print(len(l))


# for tup in l:
#     cv2.circle(img, (tup[0],tup[1]), 2, (0,255,0), -1)

# cv2.imshow('my frame', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

####################################################################################################