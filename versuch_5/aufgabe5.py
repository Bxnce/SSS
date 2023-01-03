# -*- coding: utf-8 -*-
# import redlab as rl
import numpy as np
import matplotlib.pyplot as plt


def get_in():
    pass
    # data = rl.cbVInScan(0,0,0,1000,7000,1)
    # np.save("aufgabe_5_1750.npy", data)


def plot_data():
    freqs = ["1750", "2500", "3250", "4000", "4750", "5500", "6250", "7000"]
    for i in freqs:
        data = np.load(f"aufgabe_5_{i}.npy")
        fig, ax = plt.subplots()
        ax.plot(data)
        fig.savefig(f"plots/aufgabe_5_{i}.png")


if __name__ == "__main__":
    # get_in()
    plot_data()
