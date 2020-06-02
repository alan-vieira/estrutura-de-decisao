# 28. O Hipermercado Tabajara está com uma promoção de carnes que
# é imperdível. Confira:
#
#                      Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#
# Para atender a todos os clientes, cada cliente poderá levar
# apenas um dos tipos de carne da promoção, porém não há
# limites para a quantidade de carne por cliente. Se compra
# for feita no cartão Tabajara o cliente receberá ainda um
# desconto de 5% sobre o total da compra. Escreva um programa
# que peça o tipo e a quantidade de carne comprada pelo
# usuário e gere um cupom fiscal, contendo as informações
# da compra: tipo e quantidade de carne, preço total,
# tipo de pagamento, valor do desconto e valor a pagar.

print("Favor informar o tipo de carne:")
print("F - File Duplo")
print("A - Alcatra")
print("P - Picanha")
carne = input("-> ")
print()
quantidade = float(input("Favor informar a quantidade: "))
cartao = input("Favor informar se o pagamento é com cartão de crédito Tabajara, S-Sim ou N-Não: ")

desconto = 0

#File Duplo
if(carne == "F" and quantidade <= 5):
    preco = quantidade * 4.90
    preco_desconto = preco
elif(carne == "F" and quantidade > 5):
    preco = quantidade * 5.80
    preco_desconto = preco

#Alcatra
elif(carne == "A" and quantidade <= 5):
    preco = quantidade * 5.90
    preco_desconto = preco
elif(carne == "A" and quantidade > 5):
    preco = quantidade * 6.80
    preco_desconto = preco

#Picanha
elif(carne == "P" and quantidade <= 5):
    preco = quantidade * 6.90
    preco_desconto = preco
elif(carne == "P" and quantidade > 5):
    preco = quantidade * 7.80
    preco_desconto = preco



if(cartao == "S"):
    desconto = (preco * 5) / 100
    preco_desconto = preco - desconto

print("Tipo da Carne: ", carne)
print("Quantidade de Carne: ", quantidade,"kg")
print("Preço Total: R$",preco)
if(cartao == "S"):
    print("Tipo de Pagamento: Cartão Tabajara")
else:
    print("Tipo de Pagamento: Outros")

print("Valor do desconto: R$",desconto)
print("Valor a Pagar: R$",preco_desconto)