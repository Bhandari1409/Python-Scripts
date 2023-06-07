# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:47:26 2023

@author: rohan
"""
import matplotlib.pyplot as plt
import numpy as np

Qx = [0.53,0.57,0.61,0.65,0.69, 0.73, 0.77, 0.81, 0.84, 0.85, 0.89, 0.93,0.96]
Gq = [950,4180, 7350,10250, 12840, 15000, 16577, 18505,1.9e4,20080,20986 ,2.2e4, 2.21e4]
plt.plot(Qx,Gq)
plt.grid()
plt.title("Gain vs InGaAs QW conc variation")
plt.xlabel("x varies In(x)Ga(1-x)As")
plt.ylabel("Gain cm-1")
dpi_size = 400
plt.savefig('output_Qx.png', dpi=dpi_size)
plt.show()

#Bx = np.arange(0.4, 0.5, 0.02)
Bx = np.linspace(0.4, 0.5, 6)
Gq = [23515,23535,23541,23514,23493,23464]
plt.plot(Bx,Gq)
plt.grid()
plt.title("Gain vs InGaAsP QW conc variation")
plt.xlabel("x varies In(1-x)Ga(x)As(y)P(1-y) with y = 0.65")
plt.ylabel("Gain cm-1")
dpi_size = 400
plt.savefig('output_Bx.png', dpi=dpi_size)
plt.show()

#Bx = np.arange(0.4, 0.5, 0.02)
By = np.linspace(0.3, 0.7, 6)
Gq = [23391,23433, 23452, 23454, 23369, 20529]
plt.plot(By,Gq)
plt.grid()
plt.title("Gain vs InGaAsP QW conc variation")
plt.xlabel("x varies In(1-x)Ga(x)As(y)P(1-y) with y = 0.30")
plt.ylabel("Gain cm-1")
dpi_size = 400
plt.savefig('output_By.png', dpi=dpi_size)
plt.show()