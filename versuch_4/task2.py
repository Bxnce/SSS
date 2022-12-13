import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def windowing(data):
    WINDOW_SIZE = 512
    WINDOW_OVERLAP = 256
    gauss_window = scipy.signal.windows.gaussian(512, 512 / 4)
    windows = [np.concatenate((np.zeros(i), data[i: i + WINDOW_SIZE]*gauss_window, np.zeros(len(data) - i))) for i in
               range(0, len(data) - 2*WINDOW_OVERLAP, WINDOW_OVERLAP)]

    local_ft_per_window = [np.fft.rfft(win) for win in windows]
    mean_ft = np.abs(np.array(local_ft_per_window).mean(axis=0))
    return mean_ft

def get_reference_spectrum(name):
    spectrum_list = []
    for i in range(0,5):
        spectrum_list.append(windowing(np.load(f"recorded/reference/{name}{i}.npy")))

    ref_spectrum = np.abs(np.array(spectrum_list).mean(axis=0))
    np.save(f"recorded/reference/{name}reference_spectrum.npy", ref_spectrum)

def plot_refs():
    names = ["hoch", "tief", "links", "rechts"]
    for name in names:
        fig, ax = plt.subplots()
        ax.plot(np.load(f"recorded/reference/{name}_reference_spectrum.npy"))
        ax.set_title(f"reference {name}")
        fig.show()

def pearson(ref, data_n):
    data = windowing(data_n)
    if len(ref) == len(data):
        n = len(ref)
    else:
        print(f"ref: {len(ref)} data: {len(data)}")
        raise Exception("length of reference and data must be equal")
    mir = np.mean(ref)
    mid = np.mean(data)
    sigfg = 0
    for i in range(n):
        sigfg += (((ref[i] - mir) * (data[i] - mid))/n)
    rfg = sigfg/(np.std(ref)*np.std(data))
    return rfg

def comparsion():
    names = ["hoch", "tief", "links", "rechts"]
    print("------------own pearson------------")
    for name in names:
        print("reference comparsion for: ", name)
        ref_data = np.load(f"recorded/reference/{name}_reference_spectrum.npy")
        for name2 in names:
            for i in range(0,5):
                print(f"compared with {name2}_{i}:      {pearson(ref_data, np.load(f'recorded/reference/{name2}_{i}.npy'))}")
    print("------------stats.pearsonr------------")
    for name in names:
        print("reference comparsion for: ", name)
        ref_data = np.load(f"recorded/reference/{name}_reference_spectrum.npy")
        for name2 in names:
            for i in range(0,5):
                print(f"compared with {name2}_{i}:      {stats.pearsonr(ref_data, windowing(np.load(f'recorded/test_data/{name2}_{i}.npy')))}")

def erkenner(data):
    names = ["hoch", "tief", "links", "rechts"]
    reference_list = []
    for name in names:
        reference_list.append(np.load(f"recorded/reference/{name}_reference_spectrum.npy"))
    p_res = []
    for i in reference_list:
        p_res.append(pearson(i, data))
    return names[p_res.index(max(p_res))]

if __name__ == '__main__':
    pass
    #----------------a----------------
    #get_reference_spectrum("hoch_")
    #get_reference_spectrum("tief_")
    #get_reference_spectrum("links_")
    #get_reference_spectrum("rechts_")
    #plot_refs()
    #----------------b----------------
    #comparsion()
    res = erkenner(np.load("recorded/test_data/rechts_3.npy"))
    print(res)