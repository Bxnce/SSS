import numpy as np
import math

# ------------2.2--------------------------------
# Powersupply, Feinmessgerät, Pico, Python RedLab Voltage, Python RedLab Stufe
messungen = {
    1: [1.00, 1.017, 1.022, 1.005859375, 2256],
    2: [2.00, 2.019, 2.053, 2.01171875, 2460],
    3: [3.00, 3.069, 3.097, 3.06640625, 2676],
    4: [4.00, 4.071, 4.098, 4.072265625, 2882],
    5: [5.00, 5.074, 5.098, 5.078125, 3088],
    6: [6.00, 5.981, 5.999, 5.986328125, 3274],
    7: [7.00, 7.033, 7.038, 7.041015625, 3490],
    8: [8.00, 7.988, 8.008, 7.998046875, 3684],
    9: [9.00, 9.040, 9.071, 9.0429685, 3902],
    10: [10.00, 10.044, 10.09, 9.990234375, 4094]
}


# ------------2.3--------------------------------
def messfehler():
    mf_multi = []
    mf_adw = []
    for i in range(1, 11):
        mf_multi.append(messungen[i][1] - messungen[i][2])
        mf_adw.append(messungen[i][1] - messungen[i][3])

    for i, _ in enumerate(mf_multi):
        mf_multi[i] = np.power(mf_multi[i], 2)
        mf_adw[i] = np.power(mf_adw[i], 2)

    std_multi = np.sqrt(np.abs((1 / len(messungen) - 1) * np.sum(mf_multi)))
    std_adw = np.sqrt(np.abs((1 / len(messungen) - 1) * np.sum(mf_adw)))
    print(f"Standardabweichung Multi: {std_multi}")
    print(f"Standardabweichung ADW: {std_adw}")

if __name__ == "__main__":
    messfehler()
