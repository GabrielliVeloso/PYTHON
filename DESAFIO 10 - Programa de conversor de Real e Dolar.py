#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input("Qual a quantia de dinheiro você tem na carteira? R$"))
dolar = real / 5.02
euro = real / 5.00
print(" Com R$ {:.2f} voce pode comprar US$ {:.2f}" .format(real, dolar))
print(" Com R$ {:.2f} voce pode comprar € {:.2f}." .format(real, euro))