matriz = [[1, 2], [3, 4]] #cria matrix 2x2
import numpy as np

matriz_np= np.array([
                [5,6],
                [7,8]
])

print(matriz_np)

for linha in matriz:
    for elemento in linha:
        print(elemento, end="")
    print()