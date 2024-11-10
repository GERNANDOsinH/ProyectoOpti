from generadores.salas import generador_conjunto_Salas
from generadores.asignaturas import generador_conjunto_Asignaturas
from generadores.profesores import generar_conjunto_profesores
from generadores.restricciones import generar_restricciones

rangos_asignaturas = [([40, 45], [180, 200]),
                               ([54, 58], [210, 230]),
                               ([68, 72], [250, 270]),
                               ([80, 85], [300, 320]),
                               ([95, 99], [340, 360])]
rangos_salas = [([3], [9, 11]),
                         ([4], [12, 14]),
                         ([5], [15, 17]),
                         ([6], [18, 20]),
                         ([7], [21, 23])]

cantidad_asignaturas = 35
cantidad_salas = 15
cantidad_profesores = 10

A = generador_conjunto_Asignaturas(cantidad_asignaturas)
S = generador_conjunto_Salas(cantidad_salas)
Y = generar_conjunto_profesores(cantidad_profesores, cantidad_salas)

restricciones = []

objetivo = "max: "
for a in range(1, cantidad_asignaturas + 1):
    for d in ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]:
        for s in range(1, cantidad_salas + 1):
            for p in cantidad_profesores:
                for b in range(1, 8):  # Bloques 1-7
                    objetivo += f"{A[a]['prioridad']} x_{a}_{d}_{b}_{s}_{p} + {A[a]['prioridad']} m_{a}_{d}_{b}_{s}_{p} + "

    # Eliminar la última coma
    objetivo = objetivo.rstrip(" + ")

restricciones = generar_restricciones(A, Y, S, cantidad_asignaturas, cantidad_salas, cantidad_profesores)

