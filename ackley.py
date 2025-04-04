import numpy as np
import pandas as pd
import OGA
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math

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

individuo = OGA.Individuo(
                n_variables = 2,
                limites_inf = [0,100],
                limites_sup = [0,100],
                verbose     = True
            )
            

poblacion = OGA.Poblacion(n_individuos = 50,n_variables  = 2,limites_inf  = [-32.768, -32.768,],limites_sup  = [32.768,32.768],verbose = False)
history = []
for i in range(0,100):
	#print(f"Iteracion : {i}")
	poblacion.evaluar_poblacion(funcion_objetivo = funcion_objetivo,optimizacion = "minimizar", verbose= False)
	print(f"Individuo : {poblacion.mejor_individuo.fitness}")
	history.append(abs(poblacion.mejor_individuo.fitness))
	poblacion.crear_nueva_generecion(metodo_seleccion = "tournament",elitismo = 0.1,prob_mut = 0.01, distribucion = "uniforme", verbose   = False, verbose_seleccion  = False,verbose_cruce      = False,verbose_mutacion   = False)

          
          
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(np.arange(0, len(history), 1), history)  # Plot some data on the Axes.
plt.show()       



                 
       
                                 
                                 
                                 
                                                       
