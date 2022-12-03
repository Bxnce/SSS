import numpy as np
import matplotlib.pyplot as plt
import numpy.fft

SIGNAL_TIME_LENGTH = 0.0
SIGNAL_ABTASTFREQUENZ = 0
SIGNAL_LAENGE_M = 0
SIGNAL_ABTAST_INTERVAL = 0


def change_comma_to_dot():
    for i in range(10, 73, 3):
        with open('./messungen/Pusti_hoch_1.csv', 'r') as file:
            data = file.read().replace(',', '.')
        with open('./messungen/Pusti_hoch_1.csv', 'w') as file:
            file.write(data)


def plot_some_periods(data):
    data_x = data[:, 0]  # ms
    data_y = data[:, 1]  # mV

    plt.figure(figsize=(10, 5))
    #plt.plot(data_x[4997:5997], data_y[4997:5997])
    plt.plot(data_x, data_y)
    plt.xlabel('Time')
    plt.ylabel('milliVoltage')
    #plt.xticks(np.arange(0, 10004, 0.2))
    plt.grid(True)
    plt.savefig(f"./pics/plot_task1.png")
    # Grundperiodendauer: 0.8 ms
    # Grundfrequenz: 1250 Hz
    # Signaldauer: 0.05 s (-25ms - 25ms = 50ms = 0.05s)
    # Abtastrate = 0.005 ms => Abtastfrequenz 0.000005 Sekunden = 200 kHz
    # Signallänge M = 10004
    # Abtastintervall: Δt = 0.000005 s


def fourier_transformed(data):
    data_ft = numpy.fft.fft(data[:, 1])
    spektrum = np.abs(data_ft)  # negative Werte entfernen
    frequenz = np.array([x / (SIGNAL_LAENGE_M * SIGNAL_ABTAST_INTERVAL) for x in range(0, len(spektrum), 1)])

    plt.plot(frequenz/1000, spektrum)
    plt.xlabel('Frequency in kHz')
    plt.ylabel('Amplitude in V')
    plt.grid(True)
    plt.savefig(f"./pics/plot_fourier.png")
    print(f"Grundperiodendauer: 0.8ms\nGrundfrequenz: 1250Hz\nSignaldauer: {SIGNAL_TIME_LENGTH}\nAbtastrate = {SIGNAL_ABTASTFREQUENZ}kHz\nSignallänge M = {SIGNAL_LAENGE_M}\nAbtastintervall: Δt = {SIGNAL_ABTAST_INTERVAL}s")
    print(f"Grundfrequenz aus Bild: {frequenz[numpy.argmax(spektrum)]}")


if __name__ == "__main__":
    data = np.genfromtxt('messungen/Pusti_hoch_1.csv', delimiter=';', skip_header=3)
    SIGNAL_TIME_LENGTH = (np.abs(np.min(data[:, 0])) + np.abs(np.max(data[:, 0]))) / 1000  # s
    SIGNAL_ABTASTFREQUENZ = len(data[:, 0]) / SIGNAL_TIME_LENGTH  # 200 kHz
    SIGNAL_LAENGE_M = len(data[:, 0])
    SIGNAL_ABTAST_INTERVAL = 1 / SIGNAL_ABTASTFREQUENZ  # s

    #plot_some_periods(data)
    fourier_transformed(data)
