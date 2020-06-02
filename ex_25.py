# 25. Faça um programa que faça 5 perguntas para uma
# pessoa sobre um crime. As perguntas são:
#
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
#
# O programa deve no final emitir
# uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve
# ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
# e 5 como "Assassino". Caso contrário, ele será classificado
# como "Inocente".

print("Questionário de inquérito")
print("Responda '1' para sim e '2' para não.")
print()
pergunta1 = int(input("Telefonou para a vítima? "))
pergunta2 = int(input("Esteve no local do crime? "))
pergunta3 = int(input("Mora perto da vítima? "))
pergunta4 = int(input("Devia para a vítima? "))
pergunta5 = int(input("Já trabalhou com a vítima? "))
print()

cont = 0

if(pergunta1 == 1):
    cont = 1
if(pergunta2 == 1):
    cont = cont + 1
if(pergunta3 == 1):
    cont = cont + 1
if(pergunta4 == 1):
    cont = cont + 1
if(pergunta5 == 1):
    cont = cont + 1

if(cont == 2):
    print("O interrogado é conciderado suspeito")
elif(cont == 3 or cont == 4):
    print("O interrogado é conciderado cúmplice de assassinato")
elif(cont == 5):
    print("O interrogado é conciderado assassino")
else:
    print("O interrogado é conciderado inocente")