#10 - Escreva um programa que mostre se uma pessoa tem entrada gratuita ou não. Para ter entrada gratuita é necessário que seja um domingo e a idade ser menor que 12.
idade = int(input("Digite sua idade: "))
resposta_domingo = input("Digite se a data atual é um domingo (S/N): ").lower()

eh_domingo = resposta_domingo == "s"
# entrada_gratuita = idade < 12 and eh_domingo

# print("A entrada será gratuita" if entrada_gratuita else "Entrada gratuita não aprovada")
if eh_domingo and idade < 12:
    print("A entrada será gratuita")
elif idade >= 12 and eh_domingo:
    print("Iddade além do limite da promoção.")
else:
    print("A promoção só é válida nos domingos")