#7 - Faça um código em Python que iterar sobre uma lista com pelo menos 5 frutas e mostre o seu resultado
frutas= ["mamão", "melancia", "abacate", "uva", "morango"]

for fruta in frutas:
    print(fruta)
print("-" * 15)
#8 - Com base na resposta da questão anterior, faça um código em Python que ordene todos os elementos da lista de frutas.
frutas_ordenadas = sorted(frutas)
print(frutas_ordenadas)
print("-" * 15)

#9 - Agora faça a ordenação em forma decrescente.

frutas_ordenadas_rev= sorted(frutas, reverse= True)

print(frutas_ordenadas_rev)
print("ou")
print(frutas_ordenadas[::-1])