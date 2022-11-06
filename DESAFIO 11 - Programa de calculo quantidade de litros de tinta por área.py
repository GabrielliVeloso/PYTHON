#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input("Qual a largura da sua parede:"))
alt = float(input("Qual a altura da sua parede:"))
area = larg * alt
litro = area / 2
print("Sua parede tem a dimensão de {}x{} e a área a ser pintada possui {:.2f} metros quadrados." .format(larg,alt, area))
print("Voce vai precisar de {:.2f} litros de tinta para pintar a área." .format(litro))

