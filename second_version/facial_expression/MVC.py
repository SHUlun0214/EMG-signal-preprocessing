import matplotlib.pyplot as plt
import numpy as np

def MVC(emg_t, emg_filtered, emg_action_filtered, ch_n, action_num):
    emg_max_mean = [0.10030365296250231, 0.1009650555719305, 0.24927068295800095, 0.1701831727289108, 0.11088716885417224, 0.19021115396399838, 0.054217052339193314, 0.10032496360660435]
    mvc = []
    
  
    
    # assert 0
    # plt.figure(figsize=(20,5))
    for i in range(ch_n):
        mvc.append((emg_filtered[i] / emg_max_mean[i]) * 100)

    plt.figure(figsize=(40,15))
    for i in range(ch_n):
        plt.subplot(int(ch_n/2), 2, i + 1)   
        plt.title('channel %d' %i, fontsize=10)
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