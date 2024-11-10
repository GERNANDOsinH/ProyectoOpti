def generar_restricciones(A: dict, Y: dict, S: list, modelo: list, a_index, d_index, b_index, s_index, p_index):
    generar_restricciones_asignacion(A, modelo, a_index, d_index, b_index, s_index, p_index)
    generar_restricciones_multiAsignacion(modelo, a_index, d_index, b_index, s_index, p_index)
    generar_restricciones_capacidad(A, S, modelo, a_index, d_index, b_index, s_index, p_index)
    generar_restricciones_profesores(Y, modelo, a_index, d_index, b_index, s_index, p_index)
    
def generar_restricciones_capacidad(A: dict, S: list, modelo: list, a_index, d_index, b_index, s_index, p_index):
    for a in a_index:
        for d in d_index:
            for b in b_index:
                for p in p_index:
                    for s in s_index:
                        modelo.append(f"{A[a]['n_alumnos']} x_{a}_{d}_{b}_{p}_{s}_1 + {A[a]['n_alumnos']} x_{a}_{d}_{b}_{p}_{s}_2 <= {S[s]};")

def generar_restricciones_asignacion(A: dict, modelo: list, a_index, d_index, b_index, s_index, p_index):
    for a in a_index:
        restriccion = ""
        restriccion1 = ""
        for d in d_index:
            for b in b_index:
                for p in p_index:
                    for s in s_index:
                        restriccion += f"x_{a}_{d}_{b}_{p}_{s}_1 + x_{a}_{d}_{b}_{p}_{s}_2 + "
                        restriccion1 += f"{(2 - A[a]['n_bloques'])} x_{a}_{d}_{b}_{p}_{s}_1 + {(A[a]['n_bloques'] - 1)} x_{a}_{d}_{b}_{p}_{s}_2 +"
        if 6 <= A[a]['prioridad']:
            restriccion = restriccion.rstrip(" + ") + " == 1;"
            restriccion1 = restriccion1.rstrip(" + ") + " == 1;"
        else:
            restriccion = restriccion.rstrip(" + ") + " <= 1;"
            restriccion1 = restriccion1.rstrip(" + ") + " <= 1;"
        
        modelo.append(restriccion)
        modelo.append(restriccion1)

def generar_restricciones_multiAsignacion(modelo: list, a_index, d_index, b_index, s_index, p_index):
    for d in d_index:
        for b in b_index:
            for s in s_index:
                restriccion = ""
                for a in a_index:
                    for p in p_index:
                        restriccion += f"x_{a}_{d}_{b}_{p}_{s}_1 + x_{a}_{d}_{b}_{p}_{s}_2 + "
                modelo.append(restriccion.rstrip(" + ") + " <= 1;")
            for p in p_index:
                for a in a_index:
                    for s in s_index:
                        restriccion += f"x_{a}_{d}_{b}_{p}_{s}_1 + x_{a}_{d}_{b}_{p}_{s}_2 + "
                modelo.append(restriccion.rstrip(" + ") + " <= 1;")

def generar_restricciones_profesores(Y: dict, modelo: list, a_index, d_index, b_index, s_index, p_index):
    for a in a_index:
        for d in d_index:
            for b in b_index:
                for s in s_index:
                    for p in p_index:
                        if (p not in Y):
                            continue
                        if (a not in Y[p]):
                            continue
                        if (d not in Y[p][a]):
                            continue
                        if (b not in Y[p][a][d]):
                            continue
                        modelo.append(f"x_{a}_{d}_{b}_{p}_{s}_1 + x_{a}_{d}_{b}_{p}_{s}_2 <= {Y[p][a][d][b]};")