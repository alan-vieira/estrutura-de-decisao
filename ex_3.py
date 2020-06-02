# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite 'F' para feminino ou 'M' para masculino: ")
if(sexo == "F"):
    print("Você escolheu sexo feminino.")
elif(sexo == "M"):
    print("Você escolheu sexo masculino.")
else:
    print("Você digitou o sexo inválido")