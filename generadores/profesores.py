import random

def generar_conjunto_profesores(n_profesores: int, n_estudiantes: int):
    Y = {}
    p = 1
    while p <= n_profesores:
        n = 0
        for a in range(1, n_estudiantes + 1):
            for d in ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]:
                for b in range(1, 7 + 1):
                    if (n < 28):
                        r = random.choice([0, 1])
                        n += r
                        Y[p][a][d][b] = r
        if (14 <= n):
            p += 1
    return Y