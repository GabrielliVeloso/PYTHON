a= input("Digite algo:")
print ('O tipo primitivo desse valor é ' , type(a))
print('Só tem espaçõs?',a.isspace())
print('É um número?' , a.isnumeric())
print('É alfabético?' ,a.isalpha())
print('É alfa numérico?' , a.isalnum())
print('A letra é minuscula? ' , a.islower())
print('É maiuscula?', a.isupper())
print('esta capitalizada?' , a.istitle()) # PALAVRAS MISTAS MAIUSCULA E MINUSCULA