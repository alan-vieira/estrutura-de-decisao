# 24. Faça um Programa que leia 2 números e em seguida pergunte
# ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma
# frase que diga se o número é:
#
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

numero = float(input("Digite um número: "))

print("Informe a operação desejada:")
print("'1' para par ou ímpar")
print("'2' para positivo ou negativo")
print("'3' para inteiro ou decimal")

operacao = int(input("-> "))

if(operacao == 1):
# par ou ímpar
    if(round(numero) % 2 == 0):
        print("O número digitado é par.")
    else:
        print("O número digitado é ímpar.")

elif(operacao == 2):
#positivo ou negativo
    if(numero > 0):
        print("O número digitado é positivo")
    else:
        print("O número digitado é negativo")

elif(operacao == 3):
#inteiro ou decimal
    if(numero == round(numero)):
        print("O número digitado é inteiro")
    else:
        print("O número digitado é decimal")