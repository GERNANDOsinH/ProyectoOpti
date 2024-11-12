import pulp
from generadores.salas import generador_conjunto_Salas
from generadores.asignaturas import generador_conjunto_Asignaturas
from generadores.profesores import generar_conjunto_profesores
from generadores.restricciones import generar_restricciones
from generadores.variables import generar_variables

# Parámetros de entrada
cantidad_asignaturas = 40
cantidad_salas = 9
cantidad_profesores = 10

# Generación de conjuntos
A = generador_conjunto_Asignaturas(cantidad_asignaturas)
S = generador_conjunto_Salas(cantidad_salas)
Y = generar_conjunto_profesores(cantidad_profesores, cantidad_salas)

a_index = list(A.keys())
d_index = list(range(1, 6))
b_index = list(range(1, 8))
p_index = list(range(1, cantidad_profesores + 1))
s_index = list(range(cantidad_salas))
double_index = [0, 1]

# Definición del problema
problema = pulp.LpProblem("Asignacion_Optima", pulp.LpMaximize)

# Definición de variables de decisión
x = generar_variables(A, a_index, d_index, b_index, s_index, p_index)

# Función objetivo
problema += pulp.lpSum(A[a]['prioridad'] * x[(a, d, b, s, p, A[a]['n_bloques'])]
    for a in a_index
    for d in d_index
    for b in b_index
    for s in s_index
    for p in p_index
    )

# Generación de restricciones
generar_restricciones(A, Y, S, x, problema, a_index, d_index, b_index, s_index, p_index)

problema.solve()

FO_1 = pulp.value(problema.objective)

print(f"FO: {FO_1}")