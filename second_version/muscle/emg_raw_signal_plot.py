from platform import java_ver
import matplotlib.pyplot as plt
def emg_raw_signal_plot(data):
    emg_t = data['time_stamps']         # read time series of sEMG signal
    emg_v = data['time_series']         # read amplitude of sEMG signal
    ch_n = len(emg_v[0])                # read the number of channel
    emg_t -= emg_t[0]                   # set the initial time to 0s
    emg = []
    emg_channel = []
    
    # arrange the emg_v
    for i in range(0, ch_n):
        for j in emg_v:
            emg_channel.append(j[i])
        emg.append(emg_channel)
        emg_channel = []
    emg_v = emg
    
    plt.rcParams['savefig.dpi'] = 300
    plt.figure(figsize=(20,15))
    for i in range(4,6):
        j = i + 1
        plt.subplot(2, 1, i-3)
        # plt.figure(figsize=(20,15))
        plt.title('Original Signal_channal_%d' %j, fontsize=10)
        plt.plot(emg_t, emg_v[i], linewidth=0.5, label='raw signal')
        plt.xlabel('t(s)' , fontsize=10)
        plt.ylabel('amplitude(μV)', fontsize=10)
        # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0)
    plt.tight_layout()   

    return emg_t, ch_n, emg_v,
