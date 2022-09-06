import pyxdf
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal
from pathlib import Path
#-------------------------- load the data --------------------------
data_file = Path("D:/Experiment/0726/masseter.xdf")
data, header = pyxdf.load_xdf(data_file)
data1 = data[0]    # read the trigger signal data
data2 = data[1]    # read the raw EMG signal data
sfreq = 1000       # frequency of the sample

#-------------------------- plot the trigger signal --------------------------
trigger_t = data1['time_stamps']
trigger_v = data1['time_series']
trigger_t -= trigger_t[0]            # initialize the time to 0s series
plt.rcParams['savefig.dpi'] = 300    #图片像素       200=1200*800
#plt.rcParams['figure.dpi'] = 300    #图片分辨率     300=1800*1200
plt.figure(figsize=(20,5))
plt.title('Trigger signal', fontsize=10)
plt.plot(trigger_t, trigger_v, linewidth=0.5, label='trigger signal')
plt.xlabel('t(s)' , fontsize=10)
plt.ylabel('amplitude(μV)', fontsize=10)
plt.show()
#-------------------------- plot the raw EMG signal --------------------------
emg_t = data2['time_stamps']
emg_v = data2['time_series']   # EMG signal has 16 channels
emg = []
for i in emg_v:
    emg.append(i[0])           # the first channel is the signal data of masseter
emg_t = emg_t - emg_t[0]       # initialize the time to 0s series
emg_v = emg
plt.rcParams['savefig.dpi'] = 300   #图片像素       200=1200*800
plt.figure(figsize=(20,5))
plt.title('Original Signal', fontsize=10)
plt.plot(emg_t, emg_v, linewidth=0.5, label='raw signal')
plt.xlabel('t(s)' , fontsize=10)
plt.ylabel('amplitude(μV)', fontsize=10)
plt.show()
#-------------------------- preprocess the EMG signal --------------------------
# process EMG signal: remove mean
emg_v = emg_v - np.mean(emg_v)
emg_filtered = emg
# set the parameter for filter
high_band = 25
low_band = 450
low_pass = 10 # 10
# create bandpass filter for EMG
high_band = high_band/(sfreq/2)
low_band = low_band/(sfreq/2)
b, a = scipy.signal.butter(4, [high_band,low_band], btype='bandpass')
# create lowpass filter
low_pass = low_pass/(sfreq/2)
b2, a2 = scipy.signal.butter(4, low_pass, btype='lowpass')
# process EMG signal: filter EMG and rectified
emg_filtered = abs(scipy.signal.filtfilt(b, a, emg_v))
# Apply to rectified signal to get EMG envelope
emg_filtered = scipy.signal.filtfilt(b2, a2, emg_filtered)
plt.rcParams['savefig.dpi'] = 300   #图片像素       200=1200*800
plt.figure(figsize=(20,5))
plt.title('Filtered signal', fontsize=10)
plt.plot(emg_t, emg_v, linewidth=0.5, color = 'orange', label='raw signal')
plt.plot(emg_t, emg_filtered, linewidth=0.5,color = 'blue', label='filtered signal')
plt.xlabel('t(s)' , fontsize=10)
plt.ylabel('amplitude(μV)', fontsize=10)
plt.show()
