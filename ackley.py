import numpy as np
import pandas as pd
import OGA
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math
from threading import Thread, Lock
import matplotlib.animation as animation

history = []
last_iteration = 0
max_iterations = 100
a = 20
b = 0.5
c = math.pi * 1/2
d = 2
range_length = 10 #32.768
range_delta = 0.1
number = 50

#
fig = plt.figure()
plt.style.use('_mpl-gallery')
ax = fig.add_subplot(projection='3d')
X = np.arange(-range_length, range_length, range_delta)
Y = np.arange(-range_length, range_length, range_delta)
X, Y = np.meshgrid(X, Y)

xs = []
ys = []
zs = []

ackley_mutex = Lock()

def ackley_r(data): 
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
  
#
def ackley_GA(dimension,range_length):
  print("Ejecutando GA...")
  individuo = OGA.Individuo(n_variables = dimension, limites_inf = [-range_length, -range_length], limites_sup = [range_length,range_length], verbose = True)
  poblacion = OGA.Poblacion(n_individuos = number,n_variables  = dimension,limites_inf  = [-range_length, -range_length],limites_sup  = [range_length,range_length],verbose = False)
  history_fitness = []
  for i in range(0,max_iterations):
	  print(f"Iteracion : {i}")
	  poblacion.evaluar_poblacion(funcion_objetivo = ackley_r,optimizacion = "minimizar", verbose= False)
	  #print(f"Individuo : {poblacion.mejor_individuo.fitness}")
	  history_fitness.append(abs(poblacion.mejor_individuo.fitness))
	  history.append(poblacion.mejor_individuo)
	  poblacion.crear_nueva_generecion(metodo_seleccion = "tournament",elitismo = 0.1,prob_mut = 0.01, distribucion = "uniforme", verbose   = False, verbose_seleccion  = False,verbose_cruce      = False,verbose_mutacion   = False)
	  last_iteration = i

print("Graficando funcion...")
Z = ackley_v(X,Y) 
print("Ploting...")
#ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#plt.show() 

ackley_GA_t = Thread(target=ackley_GA, args=(d,range_length))
ackley_GA_t.start()
ackley_GA_t.join()


for i in range(last_iteration,len(history)):
  xs.append(history[i].valor_variables[0])
  ys.append(history[i].valor_variables[1])
  zs.append(ackley_v(history[i].valor_variables[0],history[i].valor_variables[1]))
ackley_mutex.acquire()
for i in range(last_iteration,len(xs)):
  ax.scatter(xs[i],ys[i], zs[i])
ax.set(xticklabels=[], yticklabels=[], zticklabels=[]) 
plt.show() 
ackley_mutex.release()
      



                 
       
                                 
                                 
                                 
                                                       
