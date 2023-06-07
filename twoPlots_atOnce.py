# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:13:08 2023

@author: rohan
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate some data for the graphs
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and axis objects
fig, ax = plt.subplots()

# Plot the first graph with a solid line and blue color
ax.plot(x, y1, color='blue', linestyle='-', label='Graph 1')

# Plot the second graph with a dashed line and red color
ax.plot(x, y2, color='red', linestyle='--', label='Graph 2')

# Add a legend to distinguish the graphs
ax.legend()

# Show the figure
plt.show()
