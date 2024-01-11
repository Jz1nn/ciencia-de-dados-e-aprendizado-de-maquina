# Perceptron 1 Camada
import numpy as np

entradas = np.array([1, 9, 5])
pesos = np.array([0.8, 0.1, 0])

def Soma(e, p):
    return e.dot(p)

s = Soma(entradas, pesos)

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

saida = stepFunction(s)

print(s)
print(saida)