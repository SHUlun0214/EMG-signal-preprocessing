import matplotlib.pyplot as plt
import numpy as np
def trigger_signal_plot(data1, data2):
    trigger_t = data1['time_stamps']
    trigger_v = data1['time_series']
    emg_t = data2['time_stamps']
    trigger_v = np.divide(trigger_v, 10)
    for i in range(4, 57, 4):
        trigger_t[i] = trigger_t[i]
        trigger_t[i+2] = trigger_t[i+2] + 0.5
        trigger_v[i+1] = 0.8 
    trigger_t = trigger_t - emg_t[0]
    # print(trigger_t)
    # assert 0
    # trigger_t -= trigger_t[0]            # initialize the time to 0s series
    # trigger_v_1 = []
    # for i in trigger_v:
    #     trigger_v_1.append(i[0])
    # trigger_v = trigger_v_1
    # trigger_t = trigger_t.tolist()
    # # print(type(trigger_t))
    # # print(type(trigger_v))
    # # print(trigger_v)
    # # print(trigger_t)
    # trigger_num = len(trigger_v) - 28
    # for i in range(4, trigger_num, 1):
    #     trigger_v.pop(i)
    #     trigger_t.pop(i)
    #     # trigger_t = trigger_t.(trigger_t, i)
    # trigger_v[2] = 2
    # trigger_v[3] = 2
    
    # for i in trigger_v:
    #     if i == 3:
    #         i = 10
    #     elif i == 10:
    #         i = 3
    
    # print(trigger_v)
    # print(trigger_t)

    plt.rcParams['savefig.dpi'] = 300    
    #plt.rcParams['figure.dpi'] = 300    
    plt.figure(figsize=(20,5))
    plt.title('Trigger signal', fontsize=10)
    plt.plot(trigger_t, trigger_v, drawstyle='steps-post', linewidth=0.5, label='trigger signal')
    plt.xlabel('t(s)' , fontsize=10)
    plt.ylabel('amplitude(μV)', fontsize=10)
    
    return [trigger_t, trigger_v]
