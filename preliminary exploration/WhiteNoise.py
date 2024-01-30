'''
Exploration in generating Gaussian white noise
'''

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def white_noise(mean, std_dev, num_samples):
    return np.random.normal(mean, std_dev, num_samples)

def plot_white_noise_hist(mean, std_dev, num_samples, bins=30):
    # Generate noise
    noise = white_noise(mean, std_dev, num_samples)

    # Plot noise histogram
    plt.figure()
    plt.hist(noise, bins, density=True)
    plt.title('White Noise Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency (Hz)')
    plt.show()

def plot_white_noise_time_series(mean, std_dev, num_samples):
    # Generate noise
    noise = white_noise(mean, std_dev, num_samples)

    # Generate time axis
    time = np.arange(num_samples)

    # Plot noise as a time series
    plt.figure()
    plt.plot(time, noise)
    plt.title('White Noise Time Series')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.show()

def plot_white_noise_psd(mean, std_dev, num_samples):
    # Generate noise
    noise = white_noise(mean, std_dev, num_samples)

    # Apply Welch's Method
    (frequencies, psds) = signal.welch(noise)

    # Plot PSD graph
    plt.figure()
    plt.plot(frequencies, psds)
    plt.title('Power Spectral Density Plot of White Noise')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel(r'Power Spectral Density (1/Hz)')
    plt.show()