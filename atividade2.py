numeroChave = int(input("Digite o número chave: "))
numeroDigitado = int(input("Digite um número: "))

if numeroDigitado >= 0 and numeroDigitado <= 100:
    distancia = abs(numeroDigitado - numeroChave)
else:
    print("número maior que 100 ou menor de 0 !!")

print(f"A distancia e de {distancia}")    