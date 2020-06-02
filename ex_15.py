# 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
# informar se os valores podem ser um triângulo. Indique, caso os lados
# formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

numero1 = int(input("Digite o primeiro lado do triângulo: "))
numero2 = int(input("Digite o segundo lado do triângulo: "))
numero3 = int(input("Digite o terceiro lado do triângulo: "))

if(numero1 + numero2 > numero3 or numero2 + numero3 > numero1 or numero3 + numero1 > numero2):
    print("De acordo com os números informados, se trata de um triângulo.")
else:
    print("Não é um triângulo.")

if(numero1 == numero2 and numero2 == numero3):
    print("Triângulo Equilátero")
elif(numero1 == numero2 or numero2 == numero3 or numero3 == numero1):
    print("Triângulo Isósceles")
elif(numero1 != numero2 and numero2 != numero3):
    print("Triângulo Escaleno")