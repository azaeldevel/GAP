
import optimizacion_GA

poblacion = optimizacion_GA.Poblacion(
                n_individuos = 3,
                n_variables  = 3,
                limites_inf  = [-5,-5,-5],
                limites_sup  = [5,5,5],
                verbose = True
            )
            
poblacion.mostrar_individuos(n=2)

def funcion_objetivo(x_0, x_1, x_2):
    f= x_0**2 + x_1**2 + x_2**2
    return(f)

poblacion.evaluar_poblacion(
    funcion_objetivo = funcion_objetivo,
    optimizacion     = "minimizar",
    verbose          = True
)
