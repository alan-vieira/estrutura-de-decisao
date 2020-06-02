# 26. Um posto está vendendo combustíveis com a seguinte tabela
# de descontos:
#
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
#
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
#
# Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool,
# G-gasolina), calcule e imprima o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço
# do litro do álcool é R$ 1,90.

litro = float(input("Informe a quantidade de litros vendida: "))
combustivel = (input("Informe o tipo de combustivél, A-álcool e G-gasolina: "))

preco_gasolina = 2.50
preco_alcool = 1.90

if(litro <= 20 and combustivel == "A"):
    percente = 3
    desconto = ((litro * preco_alcool) * 3) / 100
    valor_cheio = litro * preco_alcool
    valor =  valor_cheio - desconto
elif (litro <= 20 and combustivel == "G"):
    percente = 4
    desconto = ((litro * preco_gasolina) * 4) / 100
    valor_cheio = litro * preco_gasolina
    valor = valor_cheio - desconto
elif(litro > 20 and combustivel == "A"):
    percente = 5
    desconto = ((litro * preco_alcool) * 5) / 100
    valor_cheio = litro * preco_alcool
    valor = valor_cheio - desconto
elif(litro > 20 and combustivel == "G"):
    percente = 6
    desconto = ((litro * preco_gasolina) * 6) / 100
    valor_cheio = litro * preco_gasolina
    valor = valor_cheio - desconto

print()
print("Valor sem desconto: R$", valor_cheio)
print("Desconto de", percente,"% (-): R$", desconto)
print("Total a ser pago: R$", valor)