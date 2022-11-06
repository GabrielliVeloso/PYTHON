#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print("_____LOCADORA DE VEÍCULOS VELOX____" "\nCalcule aqui o valor a ser pago na devolução do veículo alugado." )
print("-" *10)
print("METODOS DE PAGAMENTOS: Á VISTA 5% DE DESCONTO." "\nPARCELAMENTO EM 6x COM JUROS DE 2% DO TOTAL")
print("-" *10)
kmp = float(input("Digite o Km percorridos com o veículo:"))
dias = int(input("Digite a quantidade de dias do aluguel do veículo:"))
diaria = dias * 60
kmr = kmp * 0.15
total = diaria + kmr
pv = total - (total * 5 /100)
pp = total + (total * 2 / 100)
print("-" *10)
print("O valor das diárias da locação do veículo: R${:.2f}" "\nValor do KM rodado totalizou: R${:.2f}" .format(diaria, kmr))
print("-" *10)
print("O valor total a ser pago pela locação do veículo é de: R$ {:.2f}" .format(total))
print("Valor para pagamento á vista: R$ {:.2f}" .format(pv))
print("Valor para pagamento a prazo em até 6 vezes: R$ {}""\nParcelas no total de 6 x de {:.2f}" .format(pp, pp/6))