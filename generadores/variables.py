import pulp

def generar_variables(A: dict, a_index, d_index, b_index, s_index, p_index):
    x = {}
    for a in a_index:
        for d in d_index:
            for b in b_index:
                for s in s_index:
                    for p in p_index:
                            double = 1
                            if A[a]['n_bloques'] == 2:
                                double = 2
                            x[(a, d, b, s, p, double)] = pulp.LpVariable(f"x_{a}_{d}_{b}_{s}_{p}_{double}", cat='Binary')
    return x