# CRIE UM ALGORITMO QUE LEIA UM NUMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA
x = int(input("Digite um número:"))
d = x * 2
t = x * 3
r = x ** (1/2)
print("O dobro de {} vale {}." .format(x,d))
print("O triplo de {} vale {}." .format(x,t))
print("A raiz quadrada de {} é igual a {:.2f}." .format(x,r)) # (:.2f) leia: duas casas decimais flutuantes.

