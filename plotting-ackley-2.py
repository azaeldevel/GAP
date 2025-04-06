import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import axes3d

a = 20
b = 0.2
c = math.pi * 2
d = 2
range_length = 5 #32.768
range_delta = 0.1

def ackley_v(x,y):
  value_a = (np.pow(x,2) + np.pow(y,2))/d
  value_a = -b * np.sqrt(value_a)
  value_a = -a * np.exp(value_a)
  #
  value_b = np.cos(c * x) + np.cos(c * y)
  value_b = value_b/d
  value_b = np.exp(value_b)
  #
  return value_a - value_b + a - np.exp(1)



fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Make data.
X = np.arange(-range_length, range_length, range_delta)
Y = np.arange(-range_length, range_length, range_delta)
X, Y = np.meshgrid(X, Y)
Z = ackley_v(X,Y) 

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.text(0, 0, range_length, "red", color='red')

              
plt.show()
