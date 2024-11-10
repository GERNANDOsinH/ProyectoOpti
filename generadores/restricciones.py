import pulp

def generar_restricciones(A: dict, Y: dict, S: list, x, modelo, a_index, d_index, b_index, s_index, p_index):
    generar_restricciones_asignacion(A, modelo, x, a_index, d_index, b_index, s_index, p_index)
    generar_restricciones_multiAsignacion(modelo, x, a_index, d_index, b_index, s_index, p_index)
    generar_restricciones_capacidad(A, S, x, modelo, a_index, d_index, b_index, s_index, p_index)
    generar_restricciones_profesores(Y, x, modelo, a_index, d_index, b_index, s_index, p_index)
    
def generar_restricciones_capacidad(A: dict, S: list, x, modelo, a_index, d_index, b_index, s_index, p_index):
    for a in a_index:
        for d in d_index:
            for b in b_index:
                for p in p_index:
                    for s in s_index:
                        modelo += (A[a]['n_alumnos'])*(x[(a, d, b, s, p, 0)] + x[(a, d, b, s, p, 1)]) <= S[s]

def generar_restricciones_asignacion(A: dict, modelo, x, a_index, d_index, b_index, s_index, p_index):
    for a in a_index:
        if 6 <= A[a]['prioridad']:
            modelo += pulp.lpSum(x[(a, d, b, s, p, double)]
                                    for d in d_index
                                    for b in b_index
                                    for s in s_index
                                    for p in p_index
                                    for double in [0, 1]) == 1
            modelo += pulp.lpSum((2 - A[a]['n_bloques']) * x[(a, d, b, s, p, 0)] + (A[a]['n_bloques'] - 1) * x[(a, d, b, s, p, 1)]
                                         for d in d_index
                                         for b in b_index
                                         for s in s_index
                                         for p in p_index) == 1
        else:
            modelo += pulp.lpSum(x[(a, d, b, s, p, 0)] + x[(a, d, b, s, p, 1)]
                                         for d in d_index
                                         for b in b_index
                                         for s in s_index
                                         for p in p_index) <= 1
            modelo += pulp.lpSum((2 - A[a]['n_bloques']) * x[(a, d, b, s, p, 0)] + (A[a]['n_bloques'] - 1) * x[(a, d, b, s, p, 1)] for d in d_index
                                         for b in b_index
                                         for s in s_index
                                         for p in p_index) <= 1

def generar_restricciones_multiAsignacion(modelo, x, a_index, d_index, b_index, s_index, p_index):
    for d in d_index:
        for b in b_index:
            for s in s_index:
                modelo += pulp.lpSum(x[(a, d, b, s, p, 0)] + x[(a, d, b, s, p, 1)]
                                         for a in a_index
                                         for p in p_index) <= 1
    for d in d_index:
        for b in b_index:
            for p in p_index:
                modelo += pulp.lpSum(x[(a, d, b, s, p, 0)] + x[(a, d, b, s, p, 1)]
                                         for a in a_index
                                         for s in s_index) <= 1

def generar_restricciones_profesores(Y: dict, x, modelo, a_index, d_index, b_index, s_index, p_index):
    for a in a_index:
        for d in d_index:
            for b in b_index:
                for s in s_index:
                    for p in p_index:
                        print(b)
                        modelo += x[(a, d, b, s, p, 0)] + x[(a, d, b, s, p, 1)] <= Y[p][a][d][b]