import time
from datetime import datetime
import numpy
import pyaudio
from task1 import trigger
import matplotlib.pyplot as plt


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
    FORMAT = pyaudio.paInt16
    SAMPLEFREQ = 44100
    FRAMESIZE = 1024
    NOFFRAMES = 220
    TIMESTAMP = datetime.now().strftime('%Y%m%d_%H%M%S')
    COMMAND = "rechts"
    # ---------------------record reference and plot---------------------
    for i in range(0, 5):
        time.sleep(5)
        print("ready for run ", i)
        data = record()
        numpy.save(f"recorded/test_data/{COMMAND}_{i}.npy", trigger(data, 700))
        print("5s pause")
    for i in range(0, 5):
        print(i)
        data = numpy.load(f"recorded/test_data/{COMMAND}_{i}.npy")
        fig, ax = plt.subplots()
        ax.plot(data)
        ax.set_title(f"reference {i}")
        fig.show()
    # -------------------------------------------------------------------
