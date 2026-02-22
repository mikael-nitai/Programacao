# 8 - Faça um programa em Python que crie um dicionário chamado vogais que tem 
# como chaves as vogais e seus valores a posição do alfabeto.
alfabeto= "abcdefghijklmnopqrstuvwxyz"
vogais= {}
consoantes= []

for v in alfabeto:
    posicao = alfabeto.index(v)
    if v in "aeiou":
        vogais[v] = alfabeto.index(v) + 1
print(vogais)
