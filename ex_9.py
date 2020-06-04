# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

#verifica o maior número dos três
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior = numero2
elif numero3 > numero1 and numero3 > numero2:
    maior = numero3

#verifica o menor número dos três
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
elif numero2 < numero1 and numero2 < numero3:
    menor = numero2
elif numero3 < numero1 and numero3 < numero2:
    menor = numero3

#verifica o número do meio
if numero1 != maior and numero1 != menor:
    meio = numero1
elif numero2 != maior and numero2 != menor:
    meio = numero2
elif numero3 != maior and numero3 != menor:
    meio = numero3

print(maior, meio, menor)
