# -*- coding: utf-8 -*-
# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define a variable N with a new numerical value
N = 100

# Create an array S ranging from 1 to N
S = np.arange(1, N+1)

# Create an array theta ranging from 0.1 to 0.9 with 100 elements
theta = np.linspace(0.1, 0.9, 100)

# Create a 2D grid of S and theta values
S_grid, theta_grid = np.meshgrid(S, theta)

# Calculate a modified likelihood function L(theta|S) with new formula
L = S_grid * np.log(theta_grid) + (N - S_grid) * np.log(1 - theta_grid)

# Creating a 3D plot to visualize the likelihood function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
s = ax.plot_surface(S_grid, theta_grid, L, cmap='jet')

# Labeling the axes
ax.set_xlabel('S')
ax.set_ylabel('theta')
ax.set_zlabel('L')
ax.set_title('Likelihood Function L(theta|S)')
ax.view_init(65, 15)

# Saving the plot to a file
plt.savefig('s-theta-L.png')

# Uncomment the line below to display the plot
# plt.show()
