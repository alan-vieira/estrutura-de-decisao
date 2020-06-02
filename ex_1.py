# 1. Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
if(numero1 > numero2):
    print("O número", numero1, "é maior do que o número", numero2)
elif(numero2 > numero1):
    print("O número", numero1, "é menor do que o número", numero2)
else:
    print("Os números são iguais")
