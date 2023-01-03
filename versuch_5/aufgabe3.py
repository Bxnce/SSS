# konsoleneingabe, pico
import numpy as np

messungen = {
    0.5: 0.510,
    1.0: 1.025,
    1.5: 1.53,
    2.0: 2.068,
    2.5: 2.577,
    3.0: 3.082,
    3.5: 3.593,
    4.0: 4.099,
    4.5: 4.606,
    5.0: 5.132,
}

def messfehler():
    mf = []
    for i in np.arange(0.5, 5.5, 0.5):
        mf.append(i - messungen[i])
        print(mf)

    for i, _ in enumerate(mf):
        mf[i] = np.power(mf[i], 2)

    std = np.sqrt(np.abs((1 / len(mf) - 1) * np.sum(mf)))
    print(f"Standardabweichung DA-Wandlung: {std}")


if __name__ == "__main__":
    messfehler()
