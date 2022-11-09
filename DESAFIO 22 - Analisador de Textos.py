#Crie um programa que leia o nome completo de uma pessoa e mostre:
#–O nome com todas as letras maiúsculas e minúsculas.
#–Quantas letras ao todo (sem considerar espaços).
#–Quantas letras tem o primeiro nome.
# gabrielli rodrigues gomes oleksy veloso

nome = str(input("Digite seu nome completo:")) . strip() #ja elimina os espaços
print("Analisando seu nome...")
print("Seu nome com todas as letras em maiusculas e minusculas é:  {}" .format(nome.title()))
print("Seu nome em letras minusculas é:  {}" .format(nome.lower()))
print("Seu nome em letras maiusculas é:  {}" .format(nome.upper()))
print("Seu nome tem ao todo {} caracteres." .format(len(nome) - nome.count(" ")))
print("Seu primeiro nome é {} e possui {} caracteres" .format(nome[0:9], nome.find(" ")))