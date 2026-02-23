tupla = (1, [2, 3, 4], 2, 5)
print(tupla.count(2))

novaTupla= tupla + (1,)
print(novaTupla)

lista = list(novaTupla)
print(type(lista))
print(lista)

lista.pop(-1)

print(lista)