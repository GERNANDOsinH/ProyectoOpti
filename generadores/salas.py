import random

def generador_conjunto_Salas(n: int):
    ret = []

    while n > 0:
        n -= 1
        ret.append(random.randint(20, 45))
    
    return ret