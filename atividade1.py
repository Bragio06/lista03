pesoDaFruta = int(input("Digite a quatindadede Kg comprada: "))
qualFruta = int(input("Digie 0 para morango ou 1 para maçâ: "))

if qualFruta == 0:
    if pesoDaFruta < 5:
        valor = 22 * pesoDaFruta
    else:
        valor = 20 * pesoDaFruta
else:
    if pesoDaFruta < 5:
        valor = 6 * pesoDaFruta
    else:
        valor = 5 * pesoDaFruta

if pesoDaFruta > 8 or valor > 100:
    valor = valor * 0.9

print(f"A quantida total é {pesoDaFruta}kg" )
print(f"O valor a ser pago é R${valor}")
