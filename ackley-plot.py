import numpy as np
import pandas as pd
import OGA
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math
from matplotlib import cbook, cm
from matplotlib.colors import LightSource


a = 20
b = 0.2
c = math.pi * 2
#https://www.sfu.ca/~ssurjano/ackley.html                          
def funcion_objetivo(data):
  d = len(data)
  z = 0
  
  valuea = 0
  for i in range(0,d - 1):
    valuea += math.pow(data[i],2)
  valuea = valuea/d
  valuea = -b * math.sqrt(valuea)
  valuea = -a * math.exp(valuea)
  
  valueb = 0
  for i in range(0,d - 1):
    valueb += math.cos(c * data[i])
  valueb = valueb/d
  valueb = math.exp(valueb)
		
  return valuea - valueb + a + math.exp(1)

            
L = 100
data = []
for i in range(0,(2 * L) - 1):
  data.append(np.arange(-32.768, 32.768, 0.5))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Create the mesh in polar coordinates and compute corresponding Z.
r = np.linspace(0, 1.25, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)


# Express the mesh in the cartesian system.
X = np.arange(-32.768, 32.768, 0.5)
Y = np.arange(-32.768, 32.768, 0.5)
Z = []
for i in range(0,L - 1):
  Z.append(funcion_objetivo(data[i]))
  

# Plot the surface.
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)

# Tweak the limits and add latex math labels.
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')

plt.show()

