'''
Exploration of data using GWOSC libraries and data
'''

import numpy as np
from matplotlib import pyplot as plt
from gwpy.timeseries import TimeSeries
from gwpy.plot import Plot
from WhiteNoise import white_noise
from scipy.signal import welch

def plot_gaussian_time_series():
    gaussian_data = TimeSeries(white_noise(60, 4, 1000), sample_rate=10)
    gaussian_data.plot(ylabel=r'Strain').show()

def plot_real_sample_time_series():
    ldata = TimeSeries.fetch_open_data('H1', 1126259117, 1126259717)
    hdata = TimeSeries.fetch_open_data('L1', 1126259117, 1126259717)
    Plot(ldata, hdata).show()

def plot_real_sample_asd():
    data = TimeSeries.fetch_open_data('H1', 1126259117, 1126259717)
    data.plot(ylabel=r'Strain ($1/\sqrt{Hz}$)').show()
    asd = data.asd().plot(ylabel=r'Strain ($1/\sqrt{Hz}$)')
    asd.gca().set_xlim(10, 2000)
    asd.show()

def plot_real_sample_spectrogram():
    data = TimeSeries.fetch_open_data('H1', 1126259117, 1126259717)
    spectrogram = data.spectrogram(2, fftlength=1, overlap=0.5) ** 0.5

    plot = spectrogram.imshow(norm='log', vmin=5e-24, vmax=1e-19)
    axes = plot.gca()
    axes.set_yscale('log')
    axes.set_ylim(10, 2000)
    axes.colorbar(
        label=r'Gravitational-wave amplitude [strain/$\sqrt{\mathrm{Hz}}$]')
    plot.show()