import mediapipe as mp
import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from landmarks_utilities import draw_eyes_landmarks, draw_nose_landmarks
import pandas as pd
from matching import get_cordinates
from temp_extraction import get_extracterd_temperature_df


img_path = "resized_image.jpg"
df1, df2 = get_extracterd_temperature_df(img_path)

print("df1 ##############################")
print(df1)


print("df2 ##############################")
print(df2)
