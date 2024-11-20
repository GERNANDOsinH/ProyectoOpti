import pulp

def generar_variables(Y: dict, alumnos_asignatura: list, bloques_asignatura: list, S: list, a_index, s_index):
    d_index = [1, 2, 3, 4, 5]
    b_index = [1, 2, 3, 4, 5, 6, 7]
    x = {}
    for a in a_index:
        for d in d_index:
            for b in b_index:
                for s in s_index:
                    B = bloques_asignatura[a]
                    if not(a in Y and d in Y[a] and b in Y[a][d] and Y[a][d][b] == 1):
                        continue
                    if (S[s] < alumnos_asignatura[a]):
                        continue
                    if B == 2 and b == 7:
                        continue
                    x[(a, d, b, s, B)] = pulp.LpVariable(f"x_{a}_{d}_{b}_{s}_{B}", cat='Binary')
    return x