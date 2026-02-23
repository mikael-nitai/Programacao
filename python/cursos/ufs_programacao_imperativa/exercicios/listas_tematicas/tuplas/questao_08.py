#8. Faça um programa em Python que contenha uma tupla: (), e mostre quantas vezes o número 4 aparece na tupla.
tupla= (1, 2,3,4, [3,4,5],4,4,4)
print(tupla.count(4))
print("-" * 15)

contador=0

for i in tupla:
    if i == 4:
        contador += 1
    elif isinstance(i, (list, tuple)):
        contador += i.count(4)

print(contador)