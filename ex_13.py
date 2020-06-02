# 13. Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

semana = int(input("Digite o número correspondente ao dia da semana: 1 para Domingo, 2 para Segunda, 3 para Terça, 4 para Quarta, 5 para Quinta, 6 para Sexta e 7 para Sábado: "))

if(semana == 1):
    print("Domingo")
elif(semana == 2):
    print("Segunda-feira")
elif(semana == 3):
    print("Terça-feira")
elif(semana == 4):
    print("Quarta-feira")
elif(semana == 5):
    print("Quinta-feira")
elif(semana == 6):
    print("Sexta-feira")
elif(semana == 7):
    print("Sábado")
else:
    print("Valor inválido")