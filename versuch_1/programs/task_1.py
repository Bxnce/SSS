import math
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime



def read_data(filename:str):
    with open(filename, 'r') as file:
        data = np.genfromtxt(file, dtype=float, skip_header=1000, delimiter=";")
    return data

 
def get_mean(data):
    return np.mean(data[:,1])
    
def get_standard_deviation(data):
    return np.std(data[:,1])

def do_all():
    data_arr = []
    for i in range(10,73,3):
        data = read_data(f"../messungen/{i}cm.csv")
        data_arr.append((f"{i}cm", get_mean(data), get_standard_deviation(data)))
    return data_arr
        
def tuple_to_file(tuple_list):
    with open("../messungen/result_tuples.txt", 'w+') as file:
        file.write("Entfernung, Mittelwert, Standardabweichung\n")
        for tuples in tuple_list:
            file.write(str(tuples).replace("(", "").replace(")","")+"\n")

def change_comma_to_dot():
    for i in range(10,73,3):
        with open(f"../messungen/{i}cm.csv",'r') as file:
            data = file.read().replace(',', '.')
        with open(f"../messungen/{i}cm.csv",'w') as file:
            file.write(data)

def plot_data(tuple_list):
    data_x = []
    for value in tuple_list:
        data_x.append(value[1])

    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.plot(range(10,73,3), data_x)
    axes.set_title('Mean of the measurement')
    axes.set_xlabel('Distance')
    axes.set_ylabel('V')
    plt.savefig(f"../pics/task1_{str(datetime.now()).replace(' ', '_').replace(':', '_')}.png")

# Number 2
def create_log_of_data(tuple_list):
    logged_in = []
    logged_out = []
    
    for value in range(10, 73, 3):
        logged_in.append(np.log(value))
    for _, out_med, _ in tuple_list:
        logged_out.append(np.log(out_med))
    return (logged_in, logged_out)

def plot_logs(log_in, log_out):
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.plot(log_in, log_out)
    axes.set_title('Log of in and output')
    axes.set_xlabel('log(input)')
    axes.set_ylabel('log(output)')
    plt.savefig(f"../pics/task2_logarithmus_{str(datetime.now()).replace(' ', '_').replace(':', '_')}.png")  #sehr viel linearer als der erste plot

def calc_a(x_strich, y_strich):
    x_mean = np.mean(x_strich)
    y_mean = np.mean(y_strich)
    top = 0
    for i,_ in enumerate(x_strich):
        top += (x_strich[i] - x_mean) * (y_strich[i] - y_mean)
    bot = 0
    for i,_ in enumerate(x_strich):
        bot += pow(x_strich[i] - x_mean, 2)
    return top/bot

def calc_b(x_strich, y_strich, a):
    x_mean = np.mean(x_strich)
    y_mean = np.mean(y_strich)
    return y_mean - a * x_mean         

def plot_lin_reg(log_in, log_out, tuple_list):
    a = calc_a(log_in, log_out)
    b = calc_b(log_in, log_out, a)
    x = range(10,73,3)
    new_y = []
    for i in range(10,73,3):
        new_y.append(pow(math.e, b) * pow(i, a))
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.plot(x, new_y)
    axes.set_title('Linear regression with "trick" on not linear function')
    axes.set_xlabel('distance in cm')
    axes.set_ylabel('voltage in V')
    data_y = []
    for value in tuple_list:
        data_y.append(value[1])
    plt.scatter(range(10,73,3), data_y, marker="o")    
    plt.savefig(f"../pics/task2_regression_lin_not_lin_{str(datetime.now()).replace(' ', '_').replace(':', '_')}.png")  #sehr viel linearer als der erste plot

def plot_lin_reg_log(log_in, log_out):
    a = calc_a(log_in, log_out)
    b = calc_b(log_in, log_out, a)
    x = range(10,73,3)
    new_y = []
    for ind,_ in enumerate(range(10,73,3)):
        new_y.append(a*log_in[ind] + b)
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.plot(log_in, new_y)
    axes.set_title('Linear regression with log')
    axes.set_xlabel('log(distance)')
    axes.set_ylabel('log(V)')
    plt.scatter(log_in, log_out, marker="o")    
    plt.savefig(f"../pics/task2_regression_log{str(datetime.now()).replace(' ', '_').replace(':', '_')}.png")  #sehr viel linearer als der erste plot

#number 3

#def empirische_standardabweichung_x_strich():
#    data = read_data("../messungen/din_a4/laenge.csv")
#    front = 1/(len(data) - 1)
#    mean = get_mean(data)
#    back = 0
#    for i in data[:,1]:
#        back += pow(mean - i, 2)
#    std = np.sqrt(front*back)
#    return std/np.sqrt(len(data))

def empirische_standardabweichung_x_strich():
    data = read_data("../messungen/din_a4/laenge.csv")
    std = np.std(data[:,1])
    return std/np.sqrt(len(data))


def correct_form(faktor, std_faktor=1):
    data = read_data("../messungen/din_a4/laenge.csv")
    mean = get_mean(data)
    form = f"x = {mean} +- {faktor} * {std_faktor}{empirische_standardabweichung_x_strich()} = Vertrauensbereich: {mean + faktor * std_faktor * empirische_standardabweichung_x_strich()}" 
    return form

def fehlerfort(x, y, path):
    data = read_data(path)
    mean = get_mean(data)
    #abs_fehler_x = x - mean
    abs_fehler_x = empirische_standardabweichung_x_strich()
    #a = calc_a([np.log(mean)], [np.log(29.7)]) ??
    a = np.log(y) / np.log(mean)
    b = calc_b([np.log(mean)], [np.log(y)], a)
    abs_fehler_y = (pow(math.e, b) * a * pow(x, a-1)) * abs_fehler_x 
    y = pow(math.e,b)*pow(mean, a) #y von x
    return (y, abs_fehler_y)

def flaeche():
    l_y,l_f = fehlerfort(0.71093750, 29.7, "../messungen/din_a4/laenge.csv")
    b_y,b_f = fehlerfort(0.91676920, 21.0, "../messungen/din_a4/breite.csv")
    area = l_y * b_y
    messfehler = np.sqrt(pow(l_y * l_f, 2)+pow(b_y * b_f, 2))
    return f"Flaeche: {area}cm^2; Messfehler: +-{messfehler}cm^2"
    
def do_1():
    tuple_list = do_all()
    log_in, log_out = create_log_of_data(tuple_list)
    plot_data(tuple_list)
    
def do_2():
    plot_logs(log_in, log_out)
    plot_lin_reg_log(log_in, log_out)
    plot_lin_reg(log_in, log_out, tuple_list)
    
def do_3():
    print("68%::" + correct_form(1, 1))
    print("95%::" + correct_form(1.96, 2))
    cm, pm = fehlerfort(0.71093750, 29.7, "../messungen/din_a4/laenge.csv")
    print(f"{cm}cm mit absolutem Fehler: +{pm}")
    print(flaeche())
    
if __name__ == "__main__":
    #do_1()
    #do_2()
    do_3()
