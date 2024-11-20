import pulp
from .salas import generador_conjunto_Salas
from .asignaturas import generador_conjunto_Asignaturas
from .restricciones import generar_restricciones
from .variables import generar_variables

def generador_de_modelo(cantidad_salas: int, cantidad_asignaturas: int):
    bloques_asignatura, alumnos_asignatura, prioridad_asignatura, Y = generador_conjunto_Asignaturas(cantidad_asignaturas)
    S = generador_conjunto_Salas(cantidad_salas)

    a_index = list(range(len(bloques_asignatura)))
    d_index = list(range(1, 6))
    b_index = list(range(1, 8))
    s_index = list(range(cantidad_salas))

    # Definición del problema
    problema = pulp.LpProblem("Asignacion_Optima", pulp.LpMaximize)

    # Definición de variables de decisión
    x = generar_variables(Y, alumnos_asignatura, bloques_asignatura, S, a_index, s_index)

    # Función objetivo
    problema += pulp.lpSum(prioridad_asignatura[a] * x[(a, d, b, s, bloques_asignatura[a])]
        for a in a_index
        for d in d_index
        for b in b_index
        for s in s_index
        if (a, d, b, s, bloques_asignatura[a]) in x)

    # Generación de restricciones
    generar_restricciones(bloques_asignatura, prioridad_asignatura, a_index, s_index, problema, x)
    return problema