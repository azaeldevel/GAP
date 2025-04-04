import numpy as np
import pandas as pd
import OGA
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
                                        
def funcion_objetivo(x_0, x_1, x_2):
    f= x_0**2 + x_1**2 + x_2**2
    return(f)

poblacion = OGA.Poblacion(n_individuos = 50,n_variables  = 3,limites_inf  = [-5,-5,-5],limites_sup  = [5,5,5],verbose = False)
history = []
for i in range(0,100):
	print(f"Iteracion : {i}")
	poblacion.evaluar_poblacion(funcion_objetivo = funcion_objetivo,optimizacion = "minimizar", verbose= False)
	print(f"Individuo : {poblacion.mejor_individuo.fitness}")
	history.append(abs(poblacion.mejor_individuo.fitness))
	#poblacion.mostrar_individuos(n=1)
	poblacion.crear_nueva_generecion(metodo_seleccion = "tournament",elitismo = 0.1,prob_mut = 0.01, distribucion = "uniforme", verbose   = False, verbose_seleccion  = False,verbose_cruce      = False,verbose_mutacion   = False)

          
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(np.arange(0, len(history), 1), history)  # Plot some data on the Axes.
plt.show()                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                                       
