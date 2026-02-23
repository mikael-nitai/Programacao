#3 - Verifique se uma letra é vogal ou consoante.
letra=input("Digite uma letra: ")

if len(letra)>1:
    print("por favor insinra apenas uma letra")
elif not letra in "abcdefghijklmnopqrstuvwxyz":
    print("erro, insira uma letra")
elif letra in "aeiou":
    print(f"A letra {letra} é uma vogal")
else:
    print(f"a letra {letra} é uma consoante")