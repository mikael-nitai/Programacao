# 9 - Faça um programa em Python que receba uma tupla: ("Ane", Bia", "Cida"), 
# depois converta-a em uma lista e adicione o elemento "Diana". 
# Por fim, converta novamente para uma tupla.

nomes = ("Ane", "Bia", "Cida")

lista= list(nomes)
lista.append("Diana")
nomes= tuple(lista)

print(nomes)
print(type(nomes))