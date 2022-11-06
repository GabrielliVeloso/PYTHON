#faça um programa que leia o comprimento do cateto oposto e adjcente de um triangulo, calcule e mostre o comprimento da
#hipotenusa
import math
catop = float(input("COMPRIMENTO DO CATETO OPOSTO:"))
catadj = float(input("COMPRIMENTO DO CATETO ADJACENTE:"))
hipo = math.hypot(catop, catadj)
print("A HIPOTENUSA MEDE: {:.2f}" .format(hipo))

