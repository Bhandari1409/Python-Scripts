# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:04:59 2023

@author: rohan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read data from CSV file
data = pd.read_csv('Simulation_rsp.csv')
wavelength = data['wavelength um'].values[2:11]
frequency = 299792458/wavelength
responsivity = abs(data['Responsivity A/W'].values[2:11])

# Normalize the responsivity curve
normalized_responsivity = responsivity / np.max(responsivity)

# Square the normalized responsivity values to obtain the power spectrum
power_spectrum = normalized_responsivity ** 2
power_spectrum_dbm = 10 * np.log10(power_spectrum/0.001)

# Plot the power spectrum
plt.plot(frequency, power_spectrum_dbm)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectrum (dBm)')
plt.title('Power Spectrum from Responsivity Curve')
plt.show()




