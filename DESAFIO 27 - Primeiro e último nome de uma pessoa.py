# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite seu nome:"))
nomediv = nome.split()
print(nomediv)
print("Seu primeiro nome é: {}" .format(nomediv[0]))
print("Seu ultimo nome é: {}" .format(nome[len(nome)-1]))