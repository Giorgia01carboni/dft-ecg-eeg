import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

eeg = sio.loadmat("EEG_FP1.mat")
ecg = sio.loadmat("ECG.mat")

eeg = eeg["EEG_FP1"]
ecg = ecg["ECG"]

ecg_signal = ecg[:,0]
eeg_signal = eeg[:,0]

ecg_dft = np.fft.fft(ecg_signal)
eeg_dft = np.fft.fft(eeg_signal)

tot_samples_ecg = len(ecg_signal)
tot_samples_eeg = len(eeg_signal)

sampling_rate = 500

f_axis = np.arange(0, tot_samples_ecg) / tot_samples_ecg * sampling_rate
omega_axis = np.arange(0, tot_samples_eeg) / tot_samples_eeg * 2 * np.pi
t_axis = np.arange(0, tot_samples_ecg) / sampling_rate

# Magnitude of DFT. DFT plotted on Hz scale. 
# Used to map DFT results to physical frequencies
plt.plot(f_axis, np.abs(ecg_dft))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('ECG DFT')
plt.show()

plt.plot(f_axis, np.abs(eeg_dft))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('EEG DFT')
plt.show()

# Angular frequency. DFT plotted on radians scale
plt.plot(omega_axis, np.abs(ecg_dft))
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Magnitude')
plt.title('ECG DFT')
plt.show()

plt.plot(omega_axis, np.abs(eeg_dft))
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Magnitude')
plt.title('EEG DFT')
plt.show()

# Converts sample indices to time in seconds
plt.plot(t_axis, ecg_signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('ECG Signal')
plt.show()

# Use logarithmic scale to show more details
plt.plot(np.log10(np.abs(ecg_dft)), label='ECG')
plt.plot(np.log10(np.abs(eeg_dft)), label='EEG')
plt.show()
