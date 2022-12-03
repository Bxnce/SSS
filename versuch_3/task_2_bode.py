from task2 import *
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    data = Task2()

    amplitude_big = [20 * np.log10(1 / data.big_ptpbavg[x]) for x in range(0, len(data.big_ptpaavg))]

    amplitude_small = [20 * np.log10(1 / data.small_ptpbavg[x])for x in range(0, len(data.small_ptpbavg))]

    plt.plot(data.fq, amplitude_small, 'b', label='small speaker')
    plt.plot(data.fq, amplitude_big, 'y', label='big speaker')
    plt.title('Bode Amplitude')
    plt.ylabel('amplitude in dB')
    plt.xlabel('frequency in Hz')
    plt.grid(True)
    plt.semilogx()
    plt.legend()
    plt.savefig('pics/bode_amplitude-frequency.png')
    plt.show()


    # −∆t * f * 360
    phase_shift_big = [(data.big_phase[x] / 1e3 * -1) * data.fq[x] * 360
                        for x in range(0, len(data.small_phase))]

    phase_shift_small = [(data.small_phase[x] / 1e3 * -1) * data.fq[x] * 360
                          for x in range(0, len(data.small_phase))]

    plt.plot(data.fq, phase_shift_small, 'b', label='small speaker')
    plt.plot(data.fq, phase_shift_big, 'y', label='big speaker')
    plt.title('Bode Phase-Shift')
    plt.ylabel('phase shift in °')
    plt.xlabel('frequency in Hz')
    plt.grid(True)
    plt.semilogx()
    plt.legend()
    plt.savefig('pics/bode_phase-frequency.png')
    plt.show()