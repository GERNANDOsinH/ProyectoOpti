import pulp

def generar_variables(a_index, d_index, b_index, s_index, p_index, double_index):
    x = {}
    for a in a_index:
        for d in d_index:
            for b in b_index:
                for s in s_index:
                    for p in p_index:
                            for double in double_index:
                                x[(a, d, b, s, p, double)] = pulp.LpVariable(f"x_{a}_{d}_{b}_{s}_{p}_{double}", cat='Binary')
    return x