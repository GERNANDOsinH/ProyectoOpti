def generar_restricciones(A, Y, S, n_asignaturas: int, n_salas: int, n_profesores):
    restricciones = []
    for d in range(1, 6):
        for b in range(1, 8):
            for s in range(1, n_salas + 1):
                restriccion = ""
                for p in range(1, n_profesores + 1):
                    for a in range(1, n_asignaturas + 1):
                        # Para que una asignatura ocupe una sala solo si su numero de estudiantes debe ser menor o igual a la capacidad de esa sala.
                        restricciones.append(f"{A[a]['n_alumnos']} x_{a}_{d}_{b}_{s}_{p} + {A[a]['n_alumnos']} m_{a}_{d}_{b}_{s}_{p} <= {S[s]};")

                        # Para que una asignatura sea impartida por un profesor este debe poder rendir esta misma en el horario asignado.
                        restricciones.append(f"{A[a]['n_alumnos']} x_{a}_{d}_{b}_{s}_{p} + {A[a]['n_alumnos']} m_{a}_{d}_{b}_{s}_{p} <= {Y[p][a][d][b]};")
                        
                        # Una sala solo puede contener una clase a la vez.
                        restriccion = restriccion + f"x_{a}_{d}_{b}_{s}_{p} + m_{a}_{d}_{b}_{s}_{p} + "
                restriccion = restriccion.rstrip(" + ") + " <= 1;"
                restricciones.append(restriccion)
            for p in range(1, n_profesores + 1):
                restriccion = ""
                for s in range(1, n_salas + 1):
                    for a in range (1, n_asignaturas + 1):
                        # Un profesor solo puede realizar una clase en un bloque.
                        restriccion = restriccion + f"x_{a}_{d}_{b}_{s}_{p} + m_{a}_{d}_{b}_{s}_{p} + "
                restriccion = restriccion.rstrip(" + ") + " <= 1;"
                restricciones.append(restriccion)
    for a in range(1, n_asignaturas + 1):
        restriccion = ""
        restriccion_1 = ""
        for d in range(1, 6):
            for b in range(1, 8):
                for p in range(1 , n_profesores):
                    for s in range(1, n_salas + 1):
                        restriccion = restriccion + f"x_{a}_{d}_{b}_{s}_{p} + m_{a}_{d}_{b}_{s}_{p} + "
                        restriccion_1 = restriccion_1 + f"{2 - A[a]['n_bloques']} x_{a}_{d}_{b}_{s}_{p} + {A[a]['n_bloques'] - 1} m_{a}_{d}_{b}_{s}_{p} + "
        restriccion = restriccion.rstrip(" + ")
        restriccion_1 = restriccion_1.rstrip(" + ")
        if (A[a]['prioridad'] <= 5):
            restriccion = restriccion + " <= 1;"
            restriccion_1 = restriccion_1 + " <= 1;"
        else:
            restriccion = restriccion + " = 1;"
            restriccion_1 = restriccion_1 + " = 1;"
        restricciones.append(restriccion)
        restricciones.append(restriccion_1)
    return restricciones