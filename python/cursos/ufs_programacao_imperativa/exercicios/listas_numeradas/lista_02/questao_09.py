#9 - Escreva um programa que mostre se um triângulo é equilátero.
#Um triangulo equilátero tem todos os seus lados com a mesma medida
# qualquer triangulo para ser um triangulo deve ter: a + b > c e a + c > b e b + c > a
lado_a=float(input("Digíte o valor do lado A: "))
lado_b=float(input("Digíte o valor do lado B: "))
lado_c=float(input("Digíte o valor do lado C: "))

forma_triangulo= (lado_a + lado_b > lado_c and 
lado_a + lado_c > lado_b and 
lado_b + lado_c > lado_a) #testa a regra de formação de um triangulo é válida

equilatero= lado_a == lado_b == lado_c #testa se realmente é equilátero

print(f"O triângulo {lado_a},{lado_b},{lado_c} é equilátero" if forma_triangulo and equilatero else f"Os valores {lado_a},{lado_b},{lado_c} não determinam um triangulo equilátero")