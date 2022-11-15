import cv2
import numpy as np
from task2 import full_correct_pic
from task1 import task1


def find_dead_pixels():
    weiss = cv2.imread("./images/weissbild.png", 0)
    return np.argwhere(weiss[:, :] == 0)


def find_stuck_pixels():
    black = cv2.imread("./images/dunkelbild.png", 0)
    return np.argwhere(black[:, :] == 255)


def find_hot_pixels():
    black = cv2.imread("./images/dunkelbild.png", 0)
    return np.argwhere(black[:, :] > 100)


if __name__ == "__main__":
    print(find_dead_pixels(), find_stuck_pixels(), find_hot_pixels())
    full_correct_pic("./images/grau1.png") # 4.2
    task1("./images/grau1_corrected.png")  # 4.3 minimale Verbesserung der Standardabweichung
