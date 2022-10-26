import pyxdf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from PlotTrigAndSignal import PlotTriggerAndSignal
import trigger_signal_plot
import emg_raw_signal_plot
import filter_emg_signal
import MVC
from cut_trigger import cut_trigger as cuttrigger
from cut_emg import cut_emg as cutemg

#-------------------------- load the data --------------------------
data_file = Path("./DATA/1019/1019/zygomaticus.xdf")
data, header = pyxdf.load_xdf(data_file)
data1 = data[0]    # read the trigger signal data
data2 = data[1]    # read the raw EMG signal data
sfreq = 1000       # frequency of the sample


#-------------------------- plot the trigger signal ----------------------------
trigger_t, trigger_v = trigger_signal_plot.trigger_signal_plot(data1, data2)
# assert 0

#-------------------------- plot the raw EMG signal ----------------------------
emg_t, ch_n, *emg_v,  = emg_raw_signal_plot.emg_raw_signal_plot(data2)
emg_v = emg_v[0]

# -------------------------- plot trigger and signal ---------------------------
PlotTriggerAndSignal(emg_t, emg_v, trigger_t, trigger_v, ch_n)

# # #-------------------------- filter the EMG signal --------------------------
emg_filtered = filter_emg_signal.filter_emg_signal(emg_t, emg_v, sfreq)

#-------------------------- cut trigger signal -------------------------------
trigger_action_t, trigger_action_index, trigger_action_v = cuttrigger(trigger_t, trigger_v)

# chech if the trigger cutting is right or not 
# plt.rcParams['savefig.dpi'] = 300    
# #plt.rcParams['figure.dpi'] = 300    
# plt.figure(figsize=(20,5))
# plt.title('Trigger signal', fontsize=10)
# plt.plot(trigger_t, trigger_v, drawstyle='steps-post', linewidth=0.5, label='trigger signal')
# plt.scatter(trigger_action_t, trigger_action_v, linewidth=0.5, label='trigger signal')
# plt.xlabel('t(s)' , fontsize=10)
# plt.ylabel('amplitude(μV)', fontsize=10)
# #-------------------------- cut filtered emg signal -----------------------------------
emg_action_t, emg_action_v, emg_action_filtered =cutemg(emg_t, emg_v, emg_filtered, trigger_action_t, ch_n)

# -------------------------%MVC--------------------------------------------
MVC.MVC(emg_t, emg_filtered, emg_action_filtered, ch_n, action_num = 14)

plt.tight_layout()
plt.show()
