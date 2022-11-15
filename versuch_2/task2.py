import cv2
import numpy as np

BLACK_IMAGES = []


# read all black images
def read_black_images():
    global BLACK_IMAGES
    for i in range(1, 11):
        BLACK_IMAGES.append(cv2.imread(f"./images/schwarz{i}.png", 0).astype('double'))  # grayscale picture


# get a "mean" picture
def get_mean_of_pixel():
    mean_arr = BLACK_IMAGES[0].copy()
    for image in BLACK_IMAGES[1:]:
        mean_arr += image
    mean_arr = mean_arr / len(BLACK_IMAGES)
    cv2.imwrite("./images/dunkelbild.png", mean_arr)
    return mean_arr


# TASK 2 and 3 combined
def full_correct_pic(pic_path):
    dunkelbild = cv2.imread("./images/dunkelbild.png", 0)
    weissbild = cv2.imread(f"./images/weissbild.png", 0)
    weissbild = weissbild / np.mean(weissbild)
    picture = cv2.imread(pic_path, 0)
    picture = picture - dunkelbild
    picture = picture / weissbild
    cv2.imwrite(f"{pic_path.removesuffix('.png')}_corrected.png", picture)


if __name__ == "__main__":
    read_black_images()
    test = get_mean_of_pixel()
    full_correct_pic("./images/grau1.png")
