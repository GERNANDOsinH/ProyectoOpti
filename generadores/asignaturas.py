import random

def generador_conjunto_Asignaturas(n: int):
    # A[i] = {n_bloques, prioridad, n_alumnos}

    A = {}

    i = 0

    n_bloques_1 = int(n * 0.65)
    n_bloques_2 = n - n_bloques_1

    while i < 0.2 * n:
        # prioridad = random.randint(6, 10)
        prioridad = 6
        n_alumnos = random.randint(10, 40)
        r = random.randint(1, 100)
        if (r <= 65 and n_bloques_1 != 0):
            i += 1
            n_bloques_1 -= 1
            A[i] = {
                'n_bloques': 1,
                'prioridad': prioridad,
                'n_alumnos': n_alumnos,
            }
        elif (n_bloques_2 != 0):
            i += 1
            n_bloques_2 -= 1
            A[i] = {
                'n_bloques': 2,
                'prioridad': prioridad,
                'n_alumnos': n_alumnos,
            }
    
    m = i

    while i < n - m:
        # prioridad = random.randint(1, 5)
        prioridad = 1
        n_alumnos = random.randint(10, 40)
        r = random.randint(1, 100)
        if (r <= 65 and n_bloques_1 != 0):
            i += 1
            n_bloques_1 -= 1
            A[i] = {
                'n_bloques': 1,
                'prioridad': prioridad,
                'n_alumnos': n_alumnos,
            }
            
        elif (n_bloques_2 != 0):
            i += 1
            n_bloques_2 -= 1
            A[i] = {
                'n_bloques': 2,
                'prioridad': prioridad,
                'n_alumnos': n_alumnos,
            }
    
    return A