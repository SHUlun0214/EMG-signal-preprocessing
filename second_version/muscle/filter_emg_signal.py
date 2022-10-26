from turtle import shape
import matplotlib.pyplot as plt
import numpy as np
import scipy
from koikefilter import *

def filter_emg_signal(emg_t, emg_v, sfreq):
    # i = ch_n
    for i in range(len(emg_v)):
        emg_v[i] = emg_v[i] - np.mean(emg_v[i])
    emg_filtered = []
    emg_v = np.array(emg_v)

    # koike filter
    emg_filtered,_ = KoikeFilter(emg_v, sfreq)
    # print(emg_filtered.shape[0])
    # print(len(emg_t))
    # assert 0
    # KoikeFilter(emg_v, sfreq)

    # set the parameter for filter
    # high_band = 25
    # low_band = 450
    # low_pass = 10 # 10
    # # create bandpass filter for EMG
    # high_band = high_band/(sfreq/2)
    # low_band = low_band/(sfreq/2)
    # b, a = scipy.signal.butter(4, [high_band,low_band], btype='bandpass')
    # # create lowpass filter
    # low_pass = low_pass/(sfreq/2)
    # b2, a2 = scipy.signal.butter(4, low_pass, btype='lowpass')
        # # process EMG signal: filter EMG and rectified
    # emg_filtered = abs(scipy.signal.filtfilt(b, a, emg_filtered))
    # # Apply to rectified signal to get EMG envelope
    # emg_filtered = scipy.signal.filtfilt(b2, a2, emg_filtered)
    
    emg_filtered = emg_filtered.T
    # print(emg_filtered.shape)
    # print(len(emg_t))
    # print(len(emg_v[0]))
    # print(len(emg_filtered[1]))

    plt.rcParams['savefig.dpi'] = 300
    plt.figure(figsize=(20,15))
    # for i in range(emg_v.shape[0]):
    for i in range(4,6):
        # plt.subplot(emg_v.shape[0],1, i+1)
        j = i + 1
        plt.subplot(2, 1, i-3)
        plt.title('Filtered signal channel %d' %j, fontsize=10)
        plt.plot(emg_t[1000:len(emg_t)], emg_v[i][1000:len(emg_v[0])], linewidth=0.5, color = 'orange', label='raw signal')
        plt.plot(emg_t[1000:len(emg_t)], emg_filtered[i][1000:len(emg_filtered[0])], linewidth=0.5,color = 'blue', label='filtered signal')
        plt.xlabel('t(s)' , fontsize=10)
        plt.ylabel('amplitude(μV)', fontsize=10)

    
    return emg_filtered