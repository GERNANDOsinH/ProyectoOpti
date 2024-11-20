import pulp

def generar_restricciones(bloques_asignatura: list, prioridad_asignatura: list, a_index: list, s_index: list, modelo, x):
    generar_restricciones_asignacion(bloques_asignatura, prioridad_asignatura, a_index, s_index, modelo, x)
    generar_restricciones_multiAsignacion(bloques_asignatura, a_index, s_index, modelo, x)
    
def generar_restricciones_asignacion(bloques_asignatura: list, prioridad_asignatura: list, a_index: list, s_index: list, modelo, x):
    d_index = [1, 2, 3, 4, 5]
    b_index = [1, 2, 3, 4, 5, 6, 7]

    for a in a_index:
        if 6 <= prioridad_asignatura[a]:
            modelo += pulp.lpSum(x[(a, d, b, s, bloques_asignatura[a])]
                                    for d in d_index
                                    for b in b_index
                                    for s in s_index
                                    if (a, d, b, s, bloques_asignatura[a]) in x) == 1
        else:
            modelo += pulp.lpSum(x[(a, d, b, s, bloques_asignatura[a])]
                                    for d in d_index
                                    for b in b_index
                                    for s in s_index
                                    if (a, d, b, s, bloques_asignatura[a]) in x) <= 1

def generar_restricciones_multiAsignacion(bloques_asignatura: list, a_index: list, s_index: list, modelo, x):
    d_index = [1, 2, 3, 4, 5]
    b_index = [1, 2, 3, 4, 5, 6, 7]
    for d in d_index:
        for b in b_index:
            for s in s_index:
                modelo += pulp.lpSum(x[(a, d, b, s, bloques_asignatura[a])] + x[(a0, d, b - 1, s, 2)]
                                    for a in a_index
                                    for a0 in a_index
                                    if (a, d, b, s, bloques_asignatura[a]) in x
                                    if (a0, d, b - 1, s, 2) in x) <= 1