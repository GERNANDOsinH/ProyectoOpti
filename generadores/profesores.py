import random

def generar_conjunto_profesores(n_profesores: int, n_estudiantes: int):
    Y = {}
    p = 1
    while p <= n_profesores:
        n = 0
        for a in range(1, n_estudiantes + 1):
            for d in range(1, 6):
                for b in range(1, 8):
                    if (n < 28):
                        r = random.randint(0, 1)
                        n += r
                        if p not in Y:
                            Y[p] = {}
                        if a not in Y[p]:
                            Y[p][a] = {}
                        if d not in Y[p][a]:
                            Y[p][a][d] = {}
                        Y[p][a][d][b] = r
        if (14 <= n):
            p += 1
    return Y