import pulp

def generar_restricciones(A, Y, S, n_salas: int, n_profesores: int, x, modelo):
    generar_restricciones_asignacion(A, n_profesores, n_salas, modelo, x)
    generar_restricciones_capacidad(A, S, n_profesores, x, modelo)
    generar_restricciones_profesores(A, S, n_profesores, x, modelo, Y)
    generar_restricciones_multiAsignacion(A, S, n_profesores, x, modelo)

def generar_restricciones_capacidad(A, S, n_profesores, x, modelo):
    for a in A.keys():
        for d in range(1, 6):
            for b in range(1, 8):
                for p in range(1, n_profesores + 1):
                    for s in range(len(S)):
                        modelo += (A[a]['n_alumnos'])*(x[a][d][b][s][p][0] + x[a][d][b][s][p][1]) <= S[s],

def generar_restricciones_asignacion(A, n_profesores, n_salas, modelo, x):
    d_index = [1, 2, 3, 4, 5]
    b_index = [1, 2, 3, 4, 5, 6, 7]
    s_index = [{i} for i in range(n_salas)]
    p_index = [{i} for i in range(1, n_profesores + 1)]
    for a in A.keys():
        if 6 <= A[a]['prioridad']:
            modelo += pulp.lpSum(x[a][d][b][s][p][0] + x[a][d][b][s][p][1] for d in d_index
                                         for b in b_index
                                         for s in s_index
                                         for p in p_index) == 1,
            modelo += pulp.lpSum((2 - A[a]['n_bloques']) * x[a][d][b][s][p][0] + (A[a]['n_bloques'] - 1) * x[a][d][b][s][p][1] for d in d_index
                                         for b in b_index
                                         for s in s_index
                                         for p in p_index) == 1,
        else:
            modelo += pulp.lpSum(x[a][d][b][s][p][0] + x[a][d][b][s][p][1] for d in d_index
                                         for b in b_index
                                         for s in s_index
                                         for p in p_index) <= 1,
            modelo += pulp.lpSum((2 - A[a]['n_bloques']) * x[a][d][b][s][p][0] + (A[a]['n_bloques'] - 1) * x[a][d][b][s][p][1] for d in d_index
                                         for b in b_index
                                         for s in s_index
                                         for p in p_index) <= 1,

def generar_restricciones_profesores(A, S, n_profesores, x, modelo, Y):
    for a in A.keys():
        for d in range(1, 6):
            for b in range(1, 8):
                for s in range(len(S)):
                    for p in range(1, n_profesores + 1):
                        modelo += x[a][d][b][s][p][0] + x[a][d][b][s][p][1] <= Y[p][a][d][b],

def generar_restricciones_multiAsignacion(A, S, n_profesores, x, modelo):
    a_index = A.keys()
    s_index = [{i} for i in range(len(S))]
    p_index = [{i} for i in range(1, n_profesores + 1)]
    for d in range(1, 6):
        for b in range(1, 8):
            for s in s_index:
                modelo += pulp.lpSum(x[a][d][b][s][p][0] + x[a][d][b][s][p][1]
                                         for a in a_index
                                         for p in p_index) <= 1,
    for d in range(1, 6):
        for b in range(1, 8):
            for p in p_index:
                modelo += pulp.lpSum(x[a][d][b][s][p][0] + x[a][d][b][s][p][1]
                                         for a in a_index
                                         for s in s_index) <= 1,