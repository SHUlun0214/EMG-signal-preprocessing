from platform import java_ver
import matplotlib.pyplot as plt
def emg_raw_signal_plot(data):
    emg_t = data['time_stamps']
    emg_v = data['time_series']
    # ch_n = len(emg_v[0])
    ch_n = 8
    emg_t -= emg_t[0]
    emg = []
    emg_channel = []
    for i in range(0, ch_n):
        for j in emg_v:
            emg_channel.append(j[i])
        emg.append(emg_channel)
        emg_channel = []
    emg_v = emg
    # print(len(emg_v))
    """
        plt.rcParams['savefig.dpi'] = 300
    plt.figure(figsize=(40,15))
    for i in range(ch_n):
        j = i + 1
        plt.subplot(int(ch_n/2), 2, i+1)
        # plt.figure(figsize=(20,15))
        plt.title('Original Signal_channal_%d' %j, fontsize=10)
        plt.plot(emg_t, emg_v[i], linewidth=0.5, label='raw signal')
        plt.xlabel('t(s)' , fontsize=10)
        plt.ylabel('amplitude(μV)', fontsize=10)
        # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0)
    plt.tight_layout() 
    """
  

    return emg_t, ch_n, emg_v,