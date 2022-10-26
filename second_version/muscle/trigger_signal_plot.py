import matplotlib.pyplot as plt
import numpy as np
def trigger_signal_plot(data1, data2):
    trigger_t = data1['time_stamps']         # read the time series of trigger signal
    trigger_v = data1['time_series']         # read the trigger value
    emg_t = data2['time_stamps']             # read the time series of sEMG signal    
    trigger_v = np.divide(trigger_v, 10)     # set the maximun trigger value to 1.0
    
    # rearrange the trigger for cutting contraction part of muscle acitivity
    for i in range(4, 57, 4):
        trigger_t[i] = trigger_t[i]
        trigger_t[i+2] = trigger_t[i+2] + 0.5
        trigger_v[i+1] = 0.8 
    trigger_t = trigger_t - emg_t[0]         # set the trigger to have the same start time
   
    plt.rcParams['savefig.dpi'] = 300      
    plt.figure(figsize=(20,5))
    plt.title('Trigger signal', fontsize=10)
    plt.plot(trigger_t, trigger_v, drawstyle='steps-post', linewidth=0.5, label='trigger signal')
    plt.xlabel('t(s)' , fontsize=10)
    plt.ylabel('amplitude(μV)', fontsize=10)
    
    return [trigger_t, trigger_v]
