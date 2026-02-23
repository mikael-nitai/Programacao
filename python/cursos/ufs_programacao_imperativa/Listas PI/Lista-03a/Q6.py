#6 - Escreva um programa em Python que mostre a tabuada de um número qualquer, dado como entrada.
numero= int(input("Escolha um numero: "))
i = 1

for tabuada in range(10):
    tabuada= numero * i
    print(f"{numero} * {i} = {tabuada}")
    i = i + 1