# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if(numero1 > numero2 and numero1 > numero3):
    print("O primerio número é o maior dos três.")
elif(numero2 > numero1 and numero2 > numero3):
    print("O segundo número é o maior dos três.")
elif (numero3 > numero1 and numero3 > numero2):
    print("O terceiro número é o maior dos três.")

if(numero1 < numero2 and numero1 < numero3):
    print("E o primerio número é o menor dos três.")
elif(numero2 < numero1 and numero2 < numero3):
    print("E o segundo número é o menor dos três.")
elif (numero3 < numero1 and numero3 < numero2):
    print("E o terceiro número é o menor dos três.")