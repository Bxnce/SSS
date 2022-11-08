import math
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

data_arr = []
raw_data_arr = []
A = 0.0
B = 0.0


# Standard functions:
def read_data(filename: str):
    with open(filename, 'r') as file:
        data = np.genfromtxt(file, dtype=float, skip_header=1000, delimiter=";")
    return data


def get_mean(data):
    return np.mean(data[:, 1])


def get_standard_deviation(data):
    return np.std(data[:, 1])


# ----------------------------------------------------------------------------------------------------------

# Number 1
def get_mean_and_standard_deviation():
    for i in range(10, 73, 3):
        data = read_data(f"../messungen/{i}cm.csv")
        raw_data_arr.append(data)
        data_arr.append((f"{i}cm", get_mean(data), get_standard_deviation(data)))


def plot_data(tuple_list):
    data_x = []
    for value in tuple_list:
        data_x.append(value[1])

    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.plot(data_x, range(10, 73, 3))
    axes.set_title('Mean of the measurement')
    axes.set_xlabel('Volt')
    axes.set_ylabel('Distance')
    plt.savefig(f"../pics/task1_{str(datetime.now()).replace(' ', '_').replace(':', '_')}.png")


# ----------------------------------------------------------------------------------------------------------------
# Number 2
def create_log_of_data(tuple_list):
    logged_in = []
    logged_out = []

    for value in range(10, 73, 3):
        logged_in.append(np.log(value))
    for _, out_med, _ in tuple_list:
        logged_out.append(np.log(out_med))
    return logged_out, logged_in


def plot_logs(log_in, log_out):
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.plot(log_in, log_out)
    axes.set_title('Log of in and output')
    axes.set_xlabel('log(input)')
    axes.set_ylabel('log(output)')
    plt.savefig(
        f"../pics/task2_logarithmus_{str(datetime.now()).replace(' ', '_').replace(':', '_')}.png")


def calc_a(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    top = 0
    for i, _ in enumerate(x):
        top += (x[i] - x_mean) * (y[i] - y_mean)
    bot = 0
    for i, _ in enumerate(x):
        bot += pow(x[i] - x_mean, 2)
    global A
    A = top / bot


def calc_b(x, y, a):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    global B
    B = y_mean - a * x_mean


def plot_lin_reg_log(log_in, log_out):
    calc_a(log_in, log_out)
    calc_b(log_in, log_out, A)
    new_y = []
    for ind, _ in enumerate(range(10, 73, 3)):
        new_y.append(A * log_in[ind] + B)

    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.plot(log_in, new_y)
    axes.set_title('Linear regression with log')
    axes.set_xlabel('log(V)')
    axes.set_ylabel('log(distance)')
    plt.scatter(log_in, log_out, marker="o")
    plt.savefig(
        f"../pics/task2_regression_log{str(datetime.now()).replace(' ', '_').replace(':', '_')}.png")


def plot_lin_reg(tuple_list):
    x = range(10, 73, 3)
    new_y = []
    for i in range(10, 73, 3):
        new_y.append(pow(math.e, B) * pow(i, A))
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.plot(new_y, x)
    axes.set_title('Linear regression with "trick" on not linear function')
    axes.set_xlabel('voltage in V')
    axes.set_ylabel('distance in cm')
    data_y = []
    for value in tuple_list:
        data_y.append(value[1])
    plt.scatter(data_y, x, marker="o")
    plt.savefig(
        f"../pics/task2_regression_lin_not_lin_{str(datetime.now()).replace(' ', '_').replace(':', '_')}.png")


# number 3

def empirische_standardabweichung_x_strich():
    data = read_data("../messungen/din_a4/laenge.csv")
    std = np.std(data[:, 1])
    return std / np.sqrt(len(data))


def correct_form(faktor, std_faktor=1):
    data = read_data("../messungen/din_a4/laenge.csv")
    mean = get_mean(data)
    form = f"x = {mean} +- {faktor} * {std_faktor}{empirische_standardabweichung_x_strich()} = Vertrauensbereich: {mean + faktor * std_faktor * empirische_standardabweichung_x_strich()}"
    return form


def fehlerfort(path):
    data = read_data(path)
    mean = get_mean(data)
    # abs_fehler_x = x - mean
    abs_fehler_x = empirische_standardabweichung_x_strich()
    abs_fehler_y = (pow(math.e, B) * A * pow(mean, A - 1)) * abs_fehler_x
    y = pow(math.e, B) * pow(mean, A)  # y von x
    return (y, abs_fehler_y)


def flaeche():
    l_y, l_f = fehlerfort("../messungen/din_a4/laenge.csv")
    b_y, b_f = fehlerfort("../messungen/din_a4/breite.csv")
    area = l_y * b_y
    messfehler = np.sqrt(pow(l_y * b_f, 2) + pow(b_y * l_f, 2))
    return f"Flaeche: {area}cm^2; Messfehler: +-{messfehler}cm^2"


def do_1():
    get_mean_and_standard_deviation()
    plot_data(data_arr)


def do_2():
    log_in, log_out = create_log_of_data(data_arr)
    plot_logs(log_in, log_out)
    plot_lin_reg_log(log_in, log_out)
    plot_lin_reg(data_arr)


def do_3():
    print("68%::" + correct_form(1, 1))
    print("95%::" + correct_form(1.96, 2))
    cm, pm = fehlerfort("../messungen/din_a4/laenge.csv")
    print(f"{cm}cm mit absolutem Fehler: +{pm}")
    print(flaeche())


if __name__ == "__main__":
    do_1()
    do_2()
    do_3()
