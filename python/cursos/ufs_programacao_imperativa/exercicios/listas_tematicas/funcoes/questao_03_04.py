#3 - Faça uma função em Python que mostre o último caractere de uma String e 4 - Refaça a questão anterior, mas agora verifique se a string está vazia
def ultimo_caractere(texto):
    return texto[-1]

mensagem=input("Digite uma mensagem para exibir o ultimo caractere: ")
if len(mensagem) != 0:
    print(f" o ultimo caractere da string é: {ultimo_caractere(mensagem)}")
else:
    print("String vazia, por favor insira uma string válida")