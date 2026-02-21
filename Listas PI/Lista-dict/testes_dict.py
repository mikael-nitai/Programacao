dicionario = {"país" : "brasil" ,
              "estado" : "são paulo" ,
              "cidade" : "Atibaia"
}

dicionario["bairro"] = "eduardo gomes"
print(dicionario)
del dicionario["bairro"]
print(dicionario)

print("-" * 15)

dicionario["casa"] = "casa A"
print(dicionario)
removido= dicionario.pop("casa") # retorna "casa A" e apaga.
print(removido)

dicionario.clear()
print(dicionario)