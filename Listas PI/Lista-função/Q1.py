#1 - Faça uma função em Python que receba dois números e mostre o maior deles. Depois faça outra função e calcule o menor deles
def maior(n1):
    return max(n1)

def menor(n2):
    return min(n2)

numeros_maior=input("Escolha dois numeros separados por espaço para determinar o maior: ")
partes_maiores= numeros_maior.split()

numeros_maior=[]
for i in partes_maiores:
    numeros_maior.append(int(i))

if len(numeros_maior) != 2:
    print("Escolha apenas 2 números separados por espaço")
else:
    print(f"O maior número é: {maior(numeros_maior)}")

numeros_menor= input("Escolha dois numeros separados por espaço para determinar o menor: ")
partes_menores= numeros_menor.split()

numeros_menor= []

for n in partes_menores:
    numeros_menor.append(int(n))
if len(numeros_menor) != 2:
    print("Escolha apenas 2 números separados por espaço")
else:
    print(f"O menor número é {menor(numeros_menor)}")