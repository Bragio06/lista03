combustiveis = input("Digite A para álcool ou G para gasolina: ")
litros = int(input("quantos litros foi vendido:"))
if combustiveis == "G":

    if litros <= 20:
        valorDaGasolina = int(input("Digite o valor da gasolina:"))
        total = (valorDaGasolina * litros) * 0.97
        print(f"O valor total dos {litros} de Gasolina é {total}")

    elif litros > 20:
       valorDaGasolina = int(input("Digite o valor da gasolina:"))
       total = (valorDaGasolina * litros) * 0.95
       print(f"O valor total dos {litros} de Gasolina é {total}")

elif combustiveis == "A":
    if litros <= 20:
        valorDoAlcool = int(input("Digite o valor do Álcool:"))
        total = (valorDoAlcool * litros) * 0.96
        print(f"O valor total dos {litros} de Álcool é {total}")

    elif litros > 20:
        valorDoAlcool = int(input("Digite o valor do Álcool:"))
        total = (valorDoAlcool * litros) * 0.94
        print(f"O valor total dos {litros} de Álcool é {total}")
        
else:
    print("esse combustível não tem!!")


            



