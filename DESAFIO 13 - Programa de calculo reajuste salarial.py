# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o salário bruto do funcionário: R$"))
aum = salario + (salario * 15 /100)
print("O funcionário que ganhava R$ {}, com aumento de 15%, passa a receber R${:.2f}." .format(salario,aum))