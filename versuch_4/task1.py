import numpy as np
import pyaudio
import numpy
import matplotlib.pyplot as plt
from datetime import datetime

import scipy


def trigger(data, threshhold):
    data_n = []
    for i, dp in enumerate(data):
        if dp > threshhold or np.abs(dp) > threshhold:
            data_n = data[i:i + SAMPLEFREQ]  # 1s because SAMPLEFREQ is per second
            break

    return data_n


def fourier_transformed(data):
    data_ft = numpy.fft.fft(data)
    spektrum = np.abs(data_ft)  # negative Werte entfernen
    # frequenz = np.array([x / (SAMPLEFREQ) for x in range(0, len(spektrum), 1)])

    plt.plot(range(len(spektrum)), spektrum)
    plt.xlabel('Frequency in Hz')
    plt.ylabel('Amplitude in V')
    plt.grid(True)
    plt.savefig(f"./plots/plot_fourier.png")


def windowing(data):
    WINDOW_SIZE = 512
    WINDOW_OVERLAP = 256
    gauss_window = scipy.signal.windows.gaussian(512, 512 / 4)
    windows = [np.concatenate((np.zeros(i), data[i: i + WINDOW_SIZE]*gauss_window, np.zeros(len(data) - i))) for i in
               range(0, len(data) - 2*WINDOW_OVERLAP, WINDOW_OVERLAP)]

    local_ft_per_window = [np.fft.fft(win) for win in windows]
    mean_ft = np.abs(np.array(local_ft_per_window).mean(axis=0))
    return mean_ft


def plot_windowing(file_name, word):
    data = np.load('aufnahmen/Aufgabe_1a_trigger_20221212_162030.npy')
    fft = windowing(data)
    plt.plot(fft)
    plt.ylabel('amplitude')
    plt.xlabel('frequency [Hz]')
    plt.title(f'amplitude spectrum \"{word}\"')
    plt.savefig(f'plots/test_spectrum.png')
    plt.show()


if __name__ == '__main__':
    # FORMAT = pyaudio.paInt16
    # SAMPLEFREQ = 44100
    # FRAMESIZE = 1024
    # NOFFRAMES = 220
    # p = pyaudio.PyAudio()
    # print("running")
    # stream = p.open(format=FORMAT, channels=1, rate=SAMPLEFREQ,
    #                 input=True, frames_per_buffer=FRAMESIZE)
    # data = stream.read(NOFFRAMES * FRAMESIZE)
    # decoded = numpy.frombuffer(data, numpy.int16)
    # stream.stop_stream()
    # stream.close()
    # p.terminate()
    # print("done")
    # # plt.plot(decoded)
    # decoded_with_trigger = trigger(decoded, 700)
    # # plt.plot(decoded_with_trigger)
    # fourier_transformed(decoded_with_trigger)
    #
    # timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    #
    # # plt.savefig(f"plots/Aufgabe_1a_{timestamp}")
    # # plt.show()
    # print(decoded.shape)
    # np.save(f"aufnahmen/Aufgabe_1a_{timestamp}.npy", decoded)
    # np.save(f"aufnahmen/Aufgabe_1a_trigger_{timestamp}.npy", decoded_with_trigger)
    plot_windowing("cgasd", "sdasedbsfbwa")
