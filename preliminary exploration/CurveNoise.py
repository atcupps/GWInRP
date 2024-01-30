'''
Exploration in creating a noise curve for a GW detector
'''
import numpy as np
from WhiteNoise import *
from matplotlib import pyplot as plt

def noise_curvify(input):
    result = []
    for x in input:
        result.append(
            (3.63*10**-22)*((0.3*(x/40)**-6)**2 + (0.3*(x/40)**(-1))**2 + (0.1*(x/120)**0.5)**2)**(1/2)
        )
    return result

def plot_noisy_curve():
    inputs = np.linspace(10, 3000, 10000)
    noise = white_noise(1, 0.1, 10000)
    curve = noise_curvify(inputs) * noise

    plt.figure()
    plt.loglog(inputs, curve)
    plt.title('Simulated Gravitational Wave Noise Curve')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel(r'PSD (1/$\sqrt{Hz}$)')
    plt.show()

plot_noisy_curve()