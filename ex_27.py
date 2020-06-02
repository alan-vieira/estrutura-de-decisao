# 27. Uma fruteira está vendendo frutas com a seguinte tabela
# de preços:
#
#                      Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total
# da compra ultrapassar R$ 25,00, receberá ainda um desconto
# de 10% sobre este total. Escreva um algoritmo para ler a
# quantidade (em Kg) de morangos e a quantidade (em Kg) de
# maças adquiridas e escreva o valor a ser pago pelo cliente.

morango_quilo = float(input("Informe a quantidade de quilos para morango: "))
maca_quilo = float(input("Informe a quantidade de quilos para maçã: "))

#morango
if(morango_quilo <= 5):
    morango_valor = morango_quilo * 2.50

if (morango_quilo > 5 and morango_quilo < 8):
    morango_valor = morango_quilo * 2.20


#maçã
if (maca_quilo <= 5):
    maca_valor = maca_quilo * 1.80

if (maca_quilo > 5 and maca_quilo < 8):
    maca_valor = maca_quilo * 1.50


desconto = 0
valor = 0
total_fruta = morango_quilo + maca_quilo
valor_cheio = (morango_quilo * 2.20) + (maca_quilo * 1.50)

if (total_fruta >= 8 or (valor_cheio == 25)):
    desconto = (valor_cheio * 10) / 100
    valor = valor_cheio - desconto
    print()
    print("Valor sem desconto: R$", valor_cheio)
    print("Desconto (-): R$", desconto)
    print("Total a ser pago: R$", valor)
else:
    print()
    print("Valor sem desconto: R$", maca_valor + morango_valor)
    print("Desconto (-): R$", desconto)
    print("Total a ser pago: R$", maca_valor + morango_valor)
