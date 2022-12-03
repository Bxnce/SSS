import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Task2:
    def __init__(self):
        self.fq = None
        #--------------------------
        self.small_ptpaavg = None
        self.small_ptpbavg = None
        self.small_cycle_time = None
        self.small_phase = None
        #--------------------------
        self.big_ptpaavg = None
        self.big_ptpbavg = None
        self.big_cycle_time = None
        self.big_phase = None
        #--------------------------
        self.read_right_small()
        self.read_left_big()
        self.remove_string()

    def read_right_small(self):
        data = pd.read_excel("./messungen/Rechter_kleiner_Lautsprecher.xlsx")

        self.fq = np.array(data["Frequenz in Hz"])
        self.small_ptpaavg = np.array(data["Peak to Peak A Avg"])
        self.small_ptpbavg = np.array(data["Peak to Peak B Avg"])
        self.small_cycle_time = np.array(data["Cycle Time"])
        self.small_phase = np.array(data["Phasenverschiebung"])

    def read_left_big(self):
        data = pd.read_excel("./messungen/Linker_großer_Lautsprecher.xlsx")

        self.fq = np.array(data["Frequenz in Hz"])
        self.big_ptpaavg = np.array(data["Peak to Peak A Avg"].replace(" V", ""))
        self.big_ptpbavg = np.array(data["Peak to Peak B Avg"].replace(" mV", ""))
        self.big_cycle_time = np.array(data["Cycle Time"].replace(" ms", ""))
        self.big_phase = np.array(data["Phasenverschiebung"].replace(" ms", ""))

    def remove_string(self):
        tmp = []
        for x in self.big_phase:
            x = x.replace(" ms", "")
            tmp.append(x.replace(",", "."))
        self.big_phase = np.array(tmp, dtype=float)

        tmp = []
        for x in self.big_cycle_time:
            x = x.replace(" ms", "")
            x = x.replace("ms", "")
            tmp.append(x.replace(",", "."))
        self.big_cycle_time = np.array(tmp, dtype=float)

        tmp = []
        for x in self.big_ptpbavg:
            x = x.replace(" mV", "")
            tmp.append(x.replace(",", "."))
        self.big_ptpbavg = np.array(tmp, dtype=float)

        tmp = []
        for x in self.big_ptpaavg:
            x = x.replace(" V", "")
            tmp.append(x.replace(",", "."))
        self.big_ptpaavg = np.array(tmp, dtype=float)

        tmp = []
        for x in self.small_phase:
            x = x.replace(" ms", "")
            tmp.append(x.replace(",", "."))
        self.small_phase = np.array(tmp, dtype=float)

        tmp = []
        for x in self.small_cycle_time:
            x = x.replace(" ms", "")
            tmp.append(x.replace(",", "."))
        self.small_cycle_time = np.array(tmp, dtype=float)

        tmp = []
        for x in self.small_ptpaavg:
            x = x.replace(" V", "")
            x = x.replace("mV", "")
            tmp.append(x.replace(",", "."))
        self.small_ptpaavg = np.array(tmp, dtype=float)

        tmp = []
        for x in self.small_ptpbavg:
            x = x.replace(" mV", "")
            tmp.append(x.replace(",", "."))
        self.small_ptpbavg = np.array(tmp, dtype=float)

def plot(freq, amplitude, phase, name):
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle(name)
    ax1.plot(freq, amplitude, label='amplitude in mV')
    ax2.plot(freq, phase, label='phase shift in msec')
    ax1.set(ylabel='amplitude in mV')
    ax2.set(xlabel='frequency in Hz', ylabel='phase shift in msec')
    ax1.legend()
    ax2.legend()
    plt.savefig('pics/'+ name.replace(" ", "_") + '.png')

if __name__ == "__main__":
    task = Task2()
    print(type(task.big_phase[2]))
    plot(task.fq, task.small_ptpbavg, task.small_phase, "small speaker")
    plot(task.fq, task.big_ptpbavg, task.big_phase, "big speaker")