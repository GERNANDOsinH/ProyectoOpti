import pulp

def generar_variables(A, n_salas: int, n_profesores: int):
    a_index = A.keys()
    d_index = [1, 2, 3, 4, 5]
    b_index = [1, 2, 3, 4, 5, 6, 7]
    p_index = [{i} for i in range(1, n_profesores + 1)]
    s_index = [{i} for i in range(n_salas)]
    double_index = [0, 1]
    x = pulp.LpVariable.dicts("x", (a_index, d_index, b_index, s_index, p_index, double_index), cat='Binary')

    return x