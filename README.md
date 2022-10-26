# EMG-signal-preprocessing
It is a simple python code to plot the raw EMG signal, to preprocess the raw data and to plot the filtered signal.

Steps:

   1.load data
  
   2.extract and plot the trigger signal and sEMG signal
  
   3.remove mean
  
   4.band-pass filter
  
   5.low-pass filter to flatten the signal
  
   6.rectify the signal
  
   7.plot the preprocessed signal
  
   ![image](https://user-images.githubusercontent.com/112923616/189059223-d16f41bc-0566-471f-84c4-93ffcf615e1d.png)

  
2022/10/26 Update:
Previous version is used to preprocess the sEMG signal through one by one channel.
This version preprocess the signal with multi-channel and add the %MVC. 
   1. The first folder is used for processing signal when subject contrract them as possible as they can do. 
   2. The second folde is used for 8 facial muslces when subject make 6 basic facial expressions. Through %MVC, we can see how much each facial muscle participate in during facial expressions.
