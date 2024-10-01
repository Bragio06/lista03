horaParada = int(input("Digite quantas horas ficou parado: "))

if horaParada <= 2:
    valorPago = horaParada * 1
    print(f"O valor a ser pago e R$ {valorPago}")

elif horaParada >= 3 or horaParada <=5:
    tempo = horaParada - 2
    valorPago = (tempo * 1.40) + 2.00
    print(f"O valor a ser pago e R$ {valorPago}")


else:
    tempo = horaParada - 5
    valorPago = (tempo * 1.60) + 6.20
    print(f"O valor a ser pago e R$ {valorPago}")
