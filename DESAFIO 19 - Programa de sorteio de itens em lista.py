#UM PROFESSOR QUER SORTEAR UM DOS SEUS 4 ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES
#E ESCREVENDO O NOME ESCOLHIDO
import random
n1 = str(input("Digite o nome do primeiro aluno:"))
n2 = str(input("Digite o nome do segundo aluno:"))
n3 = str(input("Digite o nome do terceiro aluno:"))
n4 = str(input("Digite o nome do quarto aluno:"))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print("O aluno escolhido foi {}." .format(escolhido))
