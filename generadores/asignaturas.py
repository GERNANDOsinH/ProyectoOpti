import random

def generador_conjunto_Asignaturas(n: int):
    bloques_asignatura = []
    alumnos_asignatura = []
    prioridad_asignatura = []
    Y = {}

    i = 0

    n_bloques_1 = int(n * 0.65)
    n_bloques_2 = n - n_bloques_1

    while i < 0.2 * n:
        prioridad = random.randint(6, 10)
        n_alumnos = random.randint(10, 40)
        r = random.randint(1, 100)
        if (r <= 65 and n_bloques_1 != 0):
            i += 1
            n_bloques_1 -= 1
            bloques_asignatura.append(1)
            prioridad_asignatura.append(prioridad)
            alumnos_asignatura.append(n_alumnos)
        elif (n_bloques_2 != 0):
            i += 1
            n_bloques_2 -= 1
            bloques_asignatura.append(2)
            prioridad_asignatura.append(prioridad)
            alumnos_asignatura.append(n_alumnos)
            
    m = i

    while i < n - m:
        prioridad = random.randint(1, 5)
        n_alumnos = random.randint(10, 40)
        r = random.randint(1, 100)
        if (r <= 65 and n_bloques_1 != 0):
            i += 1
            n_bloques_1 -= 1
            bloques_asignatura.append(1)
            prioridad_asignatura.append(prioridad)
            alumnos_asignatura.append(n_alumnos)
        elif (n_bloques_2 != 0):
            i += 1
            n_bloques_2 -= 1
            bloques_asignatura.append(2)
            prioridad_asignatura.append(prioridad)
            alumnos_asignatura.append(n_alumnos)
    a = 0
    while a < n:
        k = 0
        for d in range(1, 6):
            for b in range(1, 8):
                if (k < 28):
                    r = random.randint(0, 1)
                    k += r
                    Y[a] = {}
                    Y[a][d] = {}
                    Y[a][d][b] = r
        if (14 <= k):
            a += 1

    return bloques_asignatura, alumnos_asignatura, prioridad_asignatura, Y