import time
import random
from optimizacionpython.deberestructuradedatos import buscar_numero as buscar_original
from optimizacionpython.deberestrcutradedatoscodigooptimizado import buscar_numero as buscar_optimizado


tamaños = [1000, 10000, 100000]
resultados_original = []
resultados_optimizado = []

def generar_lista_ordenada(tamaño):
    return list(range(tamaño))

def medir_tiempo(funcion, lista, objetivo):
    inicio = time.time()
    funcion(lista, objetivo)
    fin = time.time()
    return (fin - inicio) * 1000  

if __name__ == "__main__":
    for tamaño in tamaños:
        lista = generar_lista_ordenada(tamaño)
        objetivo = random.choice(lista)

        
        tiempo_original = medir_tiempo(buscar_original, lista, objetivo)
        resultados_original.append((tamaño, tiempo_original))

        
        tiempo_optimizado = medir_tiempo(buscar_optimizado, lista, objetivo)
        resultados_optimizado.append((tamaño, tiempo_optimizado))

    
    with open("resultados/resultados_original.csv", "w") as f:
        f.write("tamaño_lista,tiempo_ms\n")
        for tamaño, tiempo in resultados_original:
            f.write(f"{tamaño},{tiempo}\n")

    with open("resultados/resultados_optimizado.csv", "w") as f:
        f.write("tamaño_lista,tiempo_ms\n")
        for tamaño, tiempo in resultados_optimizado:
            f.write(f"{tamaño},{tiempo}\n")

    print("Pruebas completadas. Resultados guardados en la carpeta 'resultados'.")