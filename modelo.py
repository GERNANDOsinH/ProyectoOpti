import pulp
from generadores.salas import generador_conjunto_Salas
from generadores.asignaturas import generador_conjunto_Asignaturas
from generadores.profesores import generar_conjunto_profesores
from generadores.restricciones import generar_restricciones
from generadores.variables import generar_variables

# Parámetros de entrada
cantidad_asignaturas = 35
cantidad_salas = 15
cantidad_profesores = 10

# Generación de conjuntos
A = generador_conjunto_Asignaturas(cantidad_asignaturas)
S = generador_conjunto_Salas(cantidad_salas)
Y = generar_conjunto_profesores(cantidad_profesores, cantidad_salas)

# Definición del problema
problema = pulp.LpProblem("Asignacion_Optima", pulp.LpMaximize)

# Definición de variables de decisión
x = generar_variables(A, cantidad_salas, cantidad_profesores)


# Función objetivo
problema += pulp.lpSum(
    A[a]['prioridad'] * (x[(a, d, b, s, p, 0)] + x[(a, d, b, s, p, 1)])
    for a in A.keys()
    for d in ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    for s in range(1, cantidad_salas + 1)
    for p in range(1, cantidad_profesores + 1)
    for b in range(1, 8)
)

# Generación de restricciones
generar_restricciones(A, Y, S, cantidad_salas, cantidad_profesores, x, problema)
problema.writeLP("./modelo.lp")