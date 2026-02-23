# 7 - Faça um programa em Python que crie um dicionário onde as chaves sejam os
# números de 1 a 10 e os valores são “Par” ou “Ímpar”, a depender do número.

dicionario= {}

for i in range(1,11):
    if i % 2 == 0:
        dicionario[i] = "par"
    else: 
        dicionario[i] = "impar"

print(dicionario)