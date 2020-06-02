# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = int(input("Digite um número: "))
if(numero > 0):
    print("O número digitado é positivo")
elif(numero < 0):
    print("O número digitado é negativo")
else:
    print("O número digitado é igual a 0")