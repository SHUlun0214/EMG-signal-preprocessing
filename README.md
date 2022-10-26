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
   1. The 'muscle' folder is used for processing signal when subject contrract them as possible as they can do. 
      This version using koike-filter and band pass filter seperately and compare the result of them. The result shows that koike-filter performs well because the filtered signal is smoother. 
      ![Filtered_signal_zygomaticu_minor_major_without_Koikefilter](https://user-images.githubusercontent.com/112923616/197978392-67c57792-be92-4880-80f1-3def50067997.png)
      ![Filtered_signal_zygomaticu_minor_major](https://user-images.githubusercontent.com/112923616/197978513-b94fa4bb-e6a6-4380-a7a6-e1ebdeeddb7f.png)

   2. The 'facial expression' folder is used for 8 facial muslces when subject make 6 basic facial expressions. Through %MVC, we can see how much each facial muscle participate in during facial expressions.
   
![happy_MVC](https://user-images.githubusercontent.com/112923616/197978266-55f47d60-e3c8-43be-a4a3-ce5e92a6e0b5.png)
