# 1 - Elabore um programa que receba um número e mostre se ele é par ou ímpar.

numero=int(input("Digite um número: "))
if numero % 2 ==0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} não é par")