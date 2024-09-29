#não pode informar valores iguais
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
numero = [num1, num2, num3]

numero.sort(reverse=True)

soma = numero[0] + numero[1]
print( f"A soma dos dois maiores números são {soma}")