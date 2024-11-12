import pulp

def generar_restricciones(A: dict, Y: dict, S: list, x, modelo, a_index, d_index, b_index, s_index, p_index):
    generar_restricciones_asignacion(A, modelo, x, a_index, d_index, b_index, s_index, p_index)
    generar_restricciones_multiAsignacion(A, modelo, x, a_index, d_index, b_index, s_index, p_index)
    generar_restricciones_capacidad(A, S, x, modelo, a_index, d_index, b_index, s_index, p_index)
    generar_restricciones_profesores(A, Y, x, modelo, a_index, d_index, b_index, s_index, p_index)
    
def generar_restricciones_capacidad(A: dict, S: list, x, modelo, a_index, d_index, b_index, s_index, p_index):
    for a in a_index:
        for d in d_index:
            for b in b_index:
                for p in p_index:
                    for s in s_index:
                        if A[a]['n_bloques'] == 2:
                            modelo += (A[a]['n_alumnos']) * x[(a, d, b, s, p, 2)] <= S[s]
                        else:

                            modelo += A[a]['n_alumnos'] * x[(a, d, b, s, p, 1)] <= S[s]

def generar_restricciones_asignacion(A: dict, modelo, x, a_index, d_index, b_index, s_index, p_index):
    for a in a_index:
        double = 1
        if A[a]['n_bloques'] == 2:
            double = 2
        if 6 <= A[a]['prioridad']:
            modelo += pulp.lpSum(x[(a, d, b, s, p, double)]
                                    for d in d_index
                                    for b in b_index
                                    for s in s_index
                                    for p in p_index) == 1
        else:
            modelo += pulp.lpSum(x[(a, d, b, s, p, double)]
                                         for d in d_index
                                         for b in b_index
                                         for s in s_index
                                         for p in p_index) <= 1

def generar_restricciones_multiAsignacion(A: dict, modelo, x, a_index, d_index, b_index, s_index, p_index):
    for d in d_index:
        for b in b_index:
            for s in s_index:
                modelo += pulp.lpSum(x[(a, d, b, s, p, A[a]['n_bloques'])] for p in p_index for a in a_index) <= 1
    for d in d_index:
        for b in b_index:
            for p in p_index:
                modelo += pulp.lpSum(x[(a, d, b, s, p, A[a]['n_bloques'])] for s in s_index for a in a_index) <= 1

def generar_restricciones_profesores(A: dict, Y: dict, x, modelo, a_index, d_index, b_index, s_index, p_index):
    for a in a_index:
        for d in d_index:
            for b in b_index:
                for s in s_index:
                    for p in p_index:
                        if p in Y and a in Y[p] and d in Y[p][a] and b in Y[p][a][d]:
                            double = 1
                            if A[a]['n_bloques'] == 2:
                                double = 2
                            modelo += x[(a, d, b, s, p, double)] <= Y[p][a][d][b]