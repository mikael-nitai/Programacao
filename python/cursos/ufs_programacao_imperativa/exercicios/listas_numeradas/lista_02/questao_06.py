#6 - Verifique se um número é divisível por 2 e por 5.
num=int(input("Digite um número: "))
divisivel=num % 2 == 0 and num % 5 == 0

print(f"O número {num} é divisível por 2 e por 5." if divisivel else f"O número {num} não é dívisivel por 2 e por 5.")