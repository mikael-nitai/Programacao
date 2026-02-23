#crie uma função que recebe uma lista e retorne o maior número dessa lista #max(lista) #.append
def maior_numero(lista):
    return max(lista)

entrada = input("Digite os números a serem comparados separados por espaço: ")
partes= entrada.split()

numeros=[]
for itens in partes:
    numeros.append(int(itens))

resultado= maior_numero(numeros)
print(resultado)