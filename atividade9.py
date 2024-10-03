haste_de_Cobre = int(input("Quantidade de hastes de cobre compradas: "))
haste_de_Alumínio = int(input("Quantidade de hastes de alumínio compradas: "))

precoCobre = 2.00
precoAl    = 4.00

valor_Total = (haste_de_Cobre * precoCobre) + (haste_de_Alumínio * precoAl)
quantidade_Total = haste_de_Cobre + haste_de_Alumínio

if quantidade_Total < 5:
    desconto = 0
elif 6 <= quantidade_Total <= 15:
    desconto = valor_Total * 0.10

elif 16 <= quantidade_Total <= 20:
    desconto = valor_Total * 0.15

else:
    desconto = valor_Total * 0.20

totalPago = valor_Total - desconto

print(f"Total a ser pago: R$ {totalPago}")