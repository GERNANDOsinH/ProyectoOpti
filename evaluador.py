import pulp
import time
from generadores.modelo import generador_de_modelo
import pandas as pd

def obtener_tiempo_por_salas(n: int):
    muestras = []
    n_asignaturas = 340
    rango_salas = [3, 4, 5, 6, 7, 9, 12, 15, 18, 21]
    for n_s in rango_salas:
        start = time.time()
        for _ in range(n):
            problema = generador_de_modelo(n_s, n_asignaturas)
            problema.solve(pulp.PULP_CBC_CMD(msg=False))
        end = time.time()
        tiempo_promedio = (end - start)/n
        muestras.append([n_s, tiempo_promedio])
    df = pd.DataFrame(muestras, columns=['Numero de Salas', 'Tiempo Promedio (segundos)'])
    df.to_csv('resultados_por_salas.csv', index=False)

def obtener_tiempo_por_asignaturas(n: int):
    muestras = []
    n_salas = 21
    rango_asignaturas = [40, 54, 68, 80, 95, 180, 210, 250, 300, 340]
    for n_a in rango_asignaturas:
        start = time.time()
        for _ in range(n):
            problema = generador_de_modelo(n_salas, n_a)
            problema.solve(pulp.PULP_CBC_CMD(msg=False))
        end = time.time()
        tiempo_promedio = (end - start)/n
        muestras.append([n_a, tiempo_promedio])
    df = pd.DataFrame(muestras, columns=['Numero de Asignaturas', 'Tiempo Promedio (segundos)'])
    df.to_csv('resultados_por_asignaturas.csv', index=False)

n = int(input())

obtener_tiempo_por_asignaturas(n)
obtener_tiempo_por_salas(n)