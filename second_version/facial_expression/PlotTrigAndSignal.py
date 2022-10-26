import matplotlib.pyplot as plt
from findnearest import find_nearest
import numpy as np
def PlotTriggerAndSignal(emg_t, emg_v, trigger_t, trigger_v, ch_n):
    plt.rcParams['savefig.dpi'] = 300    
    # plt.rcParams['figure.dpi'] = 300    
    plt.figure(figsize=(40,15))
    for i in range(ch_n):
        j = i + 1
        plt.subplot(int(ch_n/2), 2, i+1)
        plt.title('Original Signal Channal_%d' %j, fontsize=10)
        plt.plot(emg_t, emg_v[i], linewidth=0.5, label='raw signal')
        plt.plot(trigger_t, trigger_v, drawstyle='steps-post', linewidth=1, label='trigger signal')
        plt.xlabel('t(s)' , fontsize=10)
        plt.ylabel('amplitude(μV)', fontsize=10)
        plt.tight_layout()

