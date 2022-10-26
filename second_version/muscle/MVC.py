import matplotlib.pyplot as plt
import numpy as np

def MVC(emg_t, emg_filtered, emg_action_filtered, ch_n, action_num):
    emg_max = []
    emg_ch_max = []
    emg_max_mean = []
    mvc = []
    emg_mvc = []
    for i in range(ch_n):
        for j in range(action_num):
            emg_ch_max.append(max(emg_action_filtered[i][j]))
        emg_max.append(emg_ch_max)
        emg_ch_max = []
    # print(len(emg_max[1]))
   
    for i in range(ch_n):
        emg_max_mean.append(np.mean(emg_max[i]))
    print(emg_max_mean[4], emg_max_mean[5])
    
    # assert 0
    plt.figure(figsize=(20,5))
    for i in range(ch_n):
        mvc.append((emg_filtered[i] / emg_max_mean[i]) * 100)

    plt.figure(figsize=(20,15))
    for i in range(4,6):
        j = i + 1
        plt.subplot(2, 1, i - 3)   
        plt.title('channel %d' %j, fontsize=10)
        plt.plot(emg_t[1000:len(emg_t)], mvc[i][1000:len(mvc[1])], linewidth=0.5,color = 'blue', label='filtered signal')
        plt.xlabel('t(s)' , fontsize=10)
        plt.ylabel('amplitude(μV)', fontsize=10)
    # for i in range(emg_filtered.shape[0]):
    #     zuida = max(emg_filtered[i])
    #     mvc = (emg_filtered[i] / zuida) * 100
    #     plt.figure(figsize=(20,5))
    #     plt.title('Filtered signal channel %d' %i, fontsize=10)
    #     plt.plot(emg_t[1000:len(emg_t)], mvc[1000:len(emg_filtered[0])], linewidth=0.5,color = 'blue', label='filtered signal')
    #     plt.xlabel('t(s)' , fontsize=10)
    #     plt.ylabel('amplitude(μV)', fontsize=10)
    #     emg_max.append(zuida)
    #     emg_mvc.append(mvc)
