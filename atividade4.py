tempoDeContribuição = int(input("Informe o seu tempo de contrubuição: "))
idade = int(input("Informe a sua idade: "))
anoAposentar = int(input("Qual ano pretende se aposentar: "))
anoAtual = int(input("Qual o seu ano atual: "))
sexo = input("Digite M para Masculino ou F para Feminino: ")
valorTotal = tempoDeContribuição + idade

if sexo == "M" and anoAposentar > anoAtual:
    if valorTotal >= (anoAposentar - anoAtual) // 2 + 95:
        print("O empregado poderá se aposentar")   
    else:
        print("O empregado não poderá se aposentar")

elif sexo == "F" and anoAposentar > anoAtual:
    if valorTotal >= (anoAposentar - anoAtual) // 2 + 85:
        print("O empregado pode se aposentar")
    else:
        print("O empregado não poderá se aposentar") 

else:
    print("Ano inválido. Não é possível cálculo")             