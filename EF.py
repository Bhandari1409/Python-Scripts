# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:13:26 2023

@author: rohan
"""



import pandas as pd
import matplotlib.pyplot as plt


# Read data from CSV file
data = pd.read_csv('Iph_ElecField_Y.csv')
distance = data['distance (um)'].values[3:70]
EF = (data['EF'].values[3:70])

# Plot the Electric Field
plt.plot(distance, EF)
plt.xlabel('distance (um)')
plt.ylabel('EF')
plt.title('Electric Field Curve')

dpi_size = 400
plt.savefig('EF.png', dpi=dpi_size)
plt.show()


