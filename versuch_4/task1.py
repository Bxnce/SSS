import numpy as np
import pyaudio
import numpy
import matplotlib.pyplot as plt
from datetime import datetime

import scipy

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220
TIMESTAMP = datetime.now().strftime('%Y%m%d_%H%M%S')

def trigger(data, threshhold):
    data_n = []
    for i, dp in enumerate(data):
        if dp > threshhold or np.abs(dp) > threshhold:
            data_n = data[i:i + SAMPLEFREQ]  # 1s because SAMPLEFREQ is per second
            break

    return data_n


def fourier_transformed(data): # Amplitudenspektrum
    data_ft = numpy.fft.fft(data)
    spektrum = np.abs(data_ft)  # negative Werte entfernen

    fig, ax = plt.subplots()
    ax.plot(range(len(spektrum)), spektrum)
    ax.set_title('amplitude spectrum without windowing')
    ax.set_xlabel('Frequency in Hz')
    ax.set_ylabel('Amplitude in V')
    ax.grid(True)
    fig.savefig("./plots/plot_fourier.png")
    fig.show()


def windowing(data):
    WINDOW_SIZE = 512
    WINDOW_OVERLAP = 256
    gauss_window = scipy.signal.windows.gaussian(512, 512 / 4)
    windows = [np.concatenate((np.zeros(i), data[i: i + WINDOW_SIZE]*gauss_window, np.zeros(len(data) - i))) for i in
               range(0, len(data) - 2*WINDOW_OVERLAP, WINDOW_OVERLAP)]

    local_ft_per_window = [np.fft.fft(win) for win in windows]
    mean_ft = np.abs(np.array(local_ft_per_window).mean(axis=0))
    return mean_ft


def plot_windowing():
    data = np.load(f'aufnahmen/Aufgabe_1a_trigger_{TIMESTAMP}.npy')
    fft = windowing(data)
    fig, ax = plt.subplots()
    ax.plot(fft)
    ax.set_ylabel('amplitude')
    ax.set_xlabel('frequency [Hz]')
    ax.set_title('amplitude spectrum n1a windowing')
    fig.savefig('plots/test_spectrum.png')
    fig.show()

def record():
    p = pyaudio.PyAudio()
    print("running")
    stream = p.open(format=FORMAT, channels=1, rate=SAMPLEFREQ,
                    input=True, frames_per_buffer=FRAMESIZE)
    data = stream.read(NOFFRAMES * FRAMESIZE)
    decoded = numpy.frombuffer(data, numpy.int16)
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("done")
    return decoded

if __name__ == '__main__':
    pass
    decoded = record()
    fig, ax = plt.subplots()
    ax.plot(decoded)
    ax.set_title('raw data')
    ax.set_xlabel('timestamps')
    ax.set_ylabel('amplitude')
    decoded_with_trigger = trigger(decoded, 700)
    fig2, ax = plt.subplots()
    ax.plot(decoded_with_trigger)
    ax.set_title('triggered')
    ax.set_xlabel('timestamps')
    ax.set_ylabel('amplitude')
    fig2.savefig(f"./plots/plot_trigger_{TIMESTAMP}.png")
    fig2.show()
    fourier_transformed(decoded_with_trigger)

    fig.savefig(f"plots/Aufgabe_1a_{TIMESTAMP}")
    fig.show()
    np.save(f"aufnahmen/Aufgabe_1a_{TIMESTAMP}.npy", decoded)
    np.save(f"aufnahmen/Aufgabe_1a_trigger_{TIMESTAMP}.npy", decoded_with_trigger)
    plot_windowing()
