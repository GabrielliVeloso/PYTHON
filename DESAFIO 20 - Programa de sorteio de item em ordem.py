#O MESMO PROFESSOR QUER SORTEAR UMA ORDEM DE APRESENTAÇÃO DE TRABALHOS. FAÇA UM PROGRAMA QUE LEIA O NOME DE 4 ALUNOS E MOSTRE A ORDEM SORTEADA
import random
n1 = str(input("Primeiro aluno:"))
n2 = str(input("Segundo aluno:"))
n3 = str(input("Terceiro aluno:"))
n4 = str(input("Quarto aluno:"))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("A ordem da apresentação sera:")
print(lista)