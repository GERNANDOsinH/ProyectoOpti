from generadores.salas import generador_conjunto_Salas
from generadores.asignaturas import generador_conjunto_Asignaturas
from generadores.profesores import generar_conjunto_profesores
from generadores.restricciones import generar_restricciones

# Parámetros de entrada
cantidad_asignaturas = 35
cantidad_salas = 15
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

modelo = []
funcion_Obj = "max: "
variables = "bin "
for a in a_index:
    for d in d_index:
        for b in b_index:
            for p in p_index:
                for s in s_index:
                    funcion_Obj += f"{A[a]['prioridad']} x_{a}_{d}_{b}_{p}_{s}_1 + {A[a]['prioridad']} x_{a}_{d}_{b}_{p}_{s}_2 + "
for a in a_index:
    for d in d_index:
        for b in b_index:
            for p in p_index:
                for s in s_index:
                    variables += f"x_{a}_{d}_{b}_{p}_{s}_1, x_{a}_{d}_{b}_{p}_{s}_2, "
                    
modelo.append(funcion_Obj.rstrip(" + ") + ";")
modelo.append(variables.rstrip(", ") + ";")

generar_restricciones(A, Y, S, modelo, a_index, d_index, b_index, s_index, p_index)

with open("modelo.lp", "w") as file:
    for line in modelo:
        file.write(line + "\n")
