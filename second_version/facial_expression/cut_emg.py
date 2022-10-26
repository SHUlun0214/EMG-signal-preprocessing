
from findnearest import find_nearest
import numpy as np
import matplotlib.pyplot as plt

def cut_emg(emg_t, emg_v, emg_filtered, trigger_action_t, ch_n):
    emg_action_index = []
    for i in trigger_action_t:
        emg_action_index.append(find_nearest(emg_t, i))
    # print(emg_action_index)
    emg_action_t = []

    for i in range(0, len(emg_action_index),2):
        emg_action_t.append(emg_t[emg_action_index[i]: emg_action_index[i+1]])
    action_num = len(emg_action_t)
    emg_filtered = emg_filtered.tolist()
    # print(action_num)

    emg_action_v = []
    emg_action_v_ch = []
    efi_action_v = []
    efi_action_v_ch = []
    for j in range(ch_n):
        for i in range(0, len(emg_action_index), 2):
            efi_action_v_ch.append(emg_filtered[j][emg_action_index[i]: emg_action_index[i+1]])
            emg_action_v_ch.append(emg_v[j][emg_action_index[i]: emg_action_index[i+1]])
        efi_action_v.append(efi_action_v_ch)
        emg_action_v.append(emg_action_v_ch)
        emg_action_v_ch = []  
        efi_action_v_ch = []


    # plt.rcParams['savefig.dpi'] = 300
    # plt.figure(figsize=(20,15))
    # for i in range(ch_n):
    #     plt.subplot(ch_n, 1, i+1)
    #     plt.plot(emg_t,emg_v[i], linewidth=0.5, color = 'orange', label='raw signal')
    #     for j in range(action_num):
    #         plt.plot(emg_action_t[j],efi_action_v[i][j], linewidth=1, color = 'blue', label='cut signal')
    #         plt.xlabel('t(s)' , fontsize=10)
    #         plt.ylabel('amplitude(μV)', fontsize=10)
    #         plt.tight_layout()

    
    # for i in range(2):
    #     for j in range(14):
    #         plt.subplot(2, 14, (i+1)*(j+1))
    #         plt.title('channel %d' %(i+1), fontsize=10)
    #         plt.plot(emg_action_t[j], emg_action_v[i][j], linewidth=0.5, color = 'orange', label='raw signal')
    #         # plt.plot(emg_action_t[j], efi_action_v[i][j], linewidth=0.5,color = 'blue', label='filtered signal')
    #         plt.xlabel('t(s)' , fontsize=10)
    #         plt.ylabel('amplitude(μV)', fontsize=10)
    #         plt.tight_layout()


    # plt.subplot(ch_n, action_num, 1)
    # plt.title('channel 1', fontsize=10)
    # plt.plot(emg_action_t[1], emg_action_v[0][1], linewidth=0.5, color = 'orange', label='raw signal')
    # plt.plot(emg_action_t[1], efi_action_v[0][1], linewidth=0.5,color = 'blue', label='filtered signal')
    # plt.xlabel('t(s)' , fontsize=10)
    # plt.ylabel('amplitude(μV)', fontsize=10)

    return emg_action_t, emg_action_v, efi_action_v

   