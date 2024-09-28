idade = int(input("Informe a idade: "))
sexo = input("Digite M para masculino ou F para feminino: ")

if sexo == "M" :
    if idade == 1:
        print("Peso provável Masculino: 8.5kg a 12.5kg")
    elif idade == 2:
        print("Peso provável Masculino:10.1kg a 15.2kg")  
    elif idade == 3:
        print("Peso provável Masculino:11.7kg a 18kg")
    else:
        print("ERRO!!!!")    
elif sexo == "F" :
    if idade == 1:
        print("Peso provável Feminino: 7.5kg a 11.5kg")
    elif idade == 2:
        print("Peso provável Feminino: 10.1kg a 15.2kg")  
    elif idade == 3:
        print("Peso provável Feminino: 11.4kg a 17.950kg")
    else:
        print("ERRO!!!!")    
else:
    print("ERRO!!!!!")             