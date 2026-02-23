#5 - Dada a matriz matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]], responda os itens a seguir:

matriz= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# qual o valor da linha 1 cooluna 2 R:6

print(matriz[1][2])


#Como alterar o valor 5 da matriz para o valor 7?
matriz[1][1]=7
print(matriz)

#Como adicionar uma nova linha na matriz?
matriz.append([10,11,12])
print(matriz)

#Como adicionar uma nova coluna na matriz?
matriz[0].append(0)
matriz[1].append(0)
matriz[2].append(0)
matriz[3].append(0)

for linha in matriz:
    for elemento in linha:
        print(elemento, end= " ")
    print()

# Como remover a terceira linha?
matriz.pop(2)
for linha in matriz:
    for elemento in linha:
        print(elemento, end= " ")
    print()