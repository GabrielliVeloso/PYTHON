# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
num = float(input("Digite um numero:"))
print("A parte inteira do número {} é {}." .format(num, trunc(num)))