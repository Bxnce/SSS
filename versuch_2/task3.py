import cv2
import numpy as np

from task2 import full_correct_pic
from task2 import maximized_contrast

WHITE_IMAGES = []


# read all white images
def read_white_images():
    global WHITE_IMAGES
    for i in range(1, 11):
        WHITE_IMAGES.append(cv2.imread(f"./images/weiss{i}.png", 0).astype('double'))  # grayscale picture


def get_mean_of_pixel():
    mean_arr = WHITE_IMAGES[0].copy()
    for image in WHITE_IMAGES[1:]:
        mean_arr += image
    mean_arr = mean_arr / len(WHITE_IMAGES)
    return mean_arr


def subtract_black_from_white():
    black = cv2.imread("./images/dunkelbild.png", 0)
    cv2.imwrite("./images/weissbild.png", (get_mean_of_pixel() - black))


if __name__ == "__main__":
    read_white_images()
    subtract_black_from_white()
    maximized_contrast("./images/weissbild.png")
