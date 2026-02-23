#faça um programa que receba 30 entradas e delas, conte quantas ssão vogais e quantas são consoantes. o programa deve aceitar letras maiusculas e minusculas
lista=[]
for i in range(5):
    entradas=input("Digite  uma letra: ").lower()
    entradas= lista.append(entradas)
    #isso deveria gerar uma lista com 30 letras
indice= 0
contador_vogal= 0
contador_consoante= 0

for contador in lista:
    if lista[indice] in ["a","e","i","o","u"]:
        contador_vogal+=1
        indice+=1
    else:
        contador_consoante+=1
        indice+=1

print(f"Em todas as entradas somadas há {contador_vogal} vogais e {contador_consoante} consoantes")