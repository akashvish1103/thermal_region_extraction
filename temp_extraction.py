import pandas as pd
from matching import get_cordinates

# df = pd.read_excel("IR000515.xlsx", header=None)
# # print(df)

# img_path = "resized_image_Screenshot 2025-06-30 125137.png.jpg"
# cordinates_left, cordinates_right = get_cordinates(img_path)



# extracted_df_left = df.iloc[cordinates_left[2][1]: cordinates_left[3][1], cordinates_left[0][0]: cordinates_left[2][0] ]
# print(extracted_df_left)

def get_extracterd_temperature_df(img_path):
    """
        This function takes img_path as INPUT and returns tow extracted corresponding temperaure dataframe for left and rigt eye,
        further we can do analysis on these dataframe (min, max, avg, std)
    """
    df = pd.read_excel("IR000515.xlsx", header=None)
    cordinates_left, cordinates_right = get_cordinates(img_path)
    extracted_df_left = df.iloc[cordinates_left[2][1]: cordinates_left[3][1], cordinates_left[0][0]: cordinates_left[2][0] ]
    extracted_df_right = df.iloc[cordinates_right[2][1]: cordinates_right[3][1], cordinates_right[0][0]: cordinates_right[2][0] ]

    # Checking the slice rows and columns length of left eyes 
    print(cordinates_left)
    print("LEFT eye row sliced length", cordinates_left[3][1] - cordinates_left[2][1])
    print("LEFT eye column sliced length", cordinates_left[3][0] - cordinates_left[1][0])

    # Checking the slice rows and columns length of right eyes 
    print(cordinates_left)
    print("RIGHT eye row sliced length", cordinates_right[3][1] - cordinates_right[2][1])
    print("RIGHT eye column sliced length", cordinates_right[3][0] - cordinates_right[1][0])

    return extracted_df_left, extracted_df_right

# img_path = "resized_image_Screenshot 2025-06-30 125137.png.jpg"
# df1, df2 = get_extracterd_temperature_df(img_path)