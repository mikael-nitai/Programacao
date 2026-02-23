#crie uma função que recebe um número e faz um contador regressivo a partir dele
def contador(n1):
    for i in range(n1,-1,-1):
       print(i)

numero_pedido= int(input("Escolha o número inicial do contador: "))
contador(numero_pedido)
