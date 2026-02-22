#9 - Faça um programa em Python que some todos os valores contidos dentro do 
# dicionário a seguir: dicionario = {“a” : 1, “b” : 2, “c” : 3}
dicionario = {"a" : 1 , "b" : 2 , "c" : 3}
soma= 0

for i in dicionario.values():
    soma += i

print(f"A soma dos valores do dicionário é {soma}.")