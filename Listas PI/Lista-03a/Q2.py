#2 - Escreva um programa em Python que receba como entrada os três valores que preencham os parâmetros do range().
inicial= int(input("Selecione um valor inicial: "))
final= int(input("Selecione um valor final: "))
incremento= int(input("Defina o incremento: "))

if incremento == 0:
    print("O incremento deve ser um valor diferente de 0")
elif inicial > final and incremento < 0 or inicial < final and incremento > 0:
    print("o intervalo não é compatível com o incremento")
else:
    for i in range(inicial, final, incremento):
        print(i)