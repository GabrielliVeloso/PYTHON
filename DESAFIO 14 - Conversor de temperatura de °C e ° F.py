#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print("CONVERSOR DE TEMPERATURAS")
tempc = float(input("Informe a temperatura em °C:"))
tempf = tempc * 1.8 + 32
print("A temperatura {}°C é igual a {}°F." .format(tempc, tempf))