# dft-ecg-eeg
Analysis on ECG and EEG signals using Discrete Fourier Transform DFT.

# Biomedical Signal Analysis

This project analyzes ECG and EEG signals using Discrete Fourier Transform (DFT) and plots their frequency spectra.

## Project Overview

The code loads two biomedical signals: 
- **ECG** (electrocardiogram): measured in millivolts (mV)
- **EEG** (electroencephalogram): measured in microvolts (μV)

The DFT (via `fft`) is used to convert the signals from the time domain to the frequency domain, and then plot the magnitude of their frequency components. Additionally, the signals in both linear and logarithmic scales are analyzed.
