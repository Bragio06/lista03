tipoDeMedia = input("Digite um tipo de média G para Geométrica, P para Ponderada, H para Harmônica e A para Aritmética: ")
vaolrX = int (input("Digite o valor de X: "))
vaolrY = int (input("Digite o valor de y: "))
vaolrZ = int (input("Digite o valor de z: "))

if tipoDeMedia == "G":
    valorDaMedia = (vaolrX * vaolrY * vaolrZ)  ** (1/3)
    print(f"A Média Geométrica foi de {valorDaMedia}")

elif tipoDeMedia == "P":
    valorDaMedia = ((vaolrX + 2) * (vaolrY + 3) * vaolrZ) // 6
    print(f"A Média Ponderada foi de {valorDaMedia}")

elif tipoDeMedia == "H":
    valorDaMedia = 1 // ((1/vaolrX) + (1/vaolrY) + (1/vaolrZ))
    print(f"A Média Harmônica foi de {valorDaMedia}")

elif tipoDeMedia == "A":
    valorDaMedia = (vaolrX + vaolrY + vaolrZ) // 3
    print(f"A Média Aritmética foi de {valorDaMedia}")

else:
    print("Erro!!! Caracter inválido!!!")   

        