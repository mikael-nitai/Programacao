#7 - Escreva um programa em Python que receba um número inteiro como entrada e valide-o. Se a entrada for inválida, solicite outra entrada.
numero_inteiro=input("Digite um número inteiro: ")
if numero_inteiro.isdigit():
    numero_inteiro=int(numero_inteiro)

else:
    print("A entrada é invalida")