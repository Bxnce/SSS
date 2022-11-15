import cv2
import sys
import numpy
import numpy as np
import pandas as pd

numpy.set_printoptions(threshold=sys.maxsize)  # print all lines of a numpy array without truncation

# ranges of the different gray zones in the picture
RANGE_1 = (0, 128)
RANGE_2 = (133, 266)
RANGE_3 = (272, 405)
RANGE_4 = (412, 544)
RANGE_5 = (549, 639)

# subpictures
gray_1 = np.array([])
gray_2 = np.array([])
gray_3 = np.array([])
gray_4 = np.array([])
gray_5 = np.array([])


def write_to_file(arr):
    with open(f"arrays/graukeil.txt", 'w+') as file:
        file.write(arr + "\n")
    pass


def remove_border(picture_array):
    offset = 5
    items_per_line = picture_array[0].size
    total_number_of_values = picture_array.size
    number_of_lines = int(total_number_of_values / items_per_line)
    return picture_array[offset: number_of_lines - offset]


def slice_sub_pictures(picture_array):
    global gray_1
    global gray_2
    global gray_3
    global gray_4
    global gray_5
    tmp1 = []
    tmp2 = []
    tmp3 = []
    tmp4 = []
    tmp5 = []
    for line in picture_array:
        tmp1.append(line[RANGE_1[0]: RANGE_1[1]])
        tmp2.append(line[RANGE_2[0]: RANGE_2[1]])
        tmp3.append(line[RANGE_3[0]: RANGE_3[1]])
        tmp4.append(line[RANGE_4[0]: RANGE_4[1]])
        tmp5.append(line[RANGE_5[0]: RANGE_5[1]])
    gray_1 = np.array(tmp1)
    gray_2 = np.array(tmp2)
    gray_3 = np.array(tmp3)
    gray_4 = np.array(tmp4)
    gray_5 = np.array(tmp5)


def task1(pic_path):
    graukeil = cv2.imread(pic_path, 0)
    graukeil_ohne_rand = remove_border(graukeil)
    slice_sub_pictures(graukeil_ohne_rand)

    hori = np.concatenate((graukeil_ohne_rand, gray_1), axis=1)
    hori = np.concatenate((hori, gray_2), axis=1)
    hori = np.concatenate((hori, gray_3), axis=1)
    hori = np.concatenate((hori, gray_4), axis=1)
    hori = np.concatenate((hori, gray_5), axis=1)

    cv2.imshow('image', hori)
    cv2.waitKey(0)

    df = pd.DataFrame([[np.mean(gray_1), np.std(gray_1)], [np.mean(gray_2), np.std(gray_2)], [np.mean(gray_3),
                                                                                              np.std(gray_3)],
                       [np.mean(gray_4), np.std(gray_4)], [np.mean(gray_5), np.std(gray_5)]],
                      index=["gray_1", "gray_2", "gray_3", "gray_4", "gray_5"], columns=["mean", "std"])

    df.to_excel(f'{pic_path}.xlsx')

if __name__ == "__main__":
    task1("./images/grau1.png")