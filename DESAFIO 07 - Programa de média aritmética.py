# DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE SUA MÉDIA
n1 = float(input("Digite a nota da PROVA 1:")) #não usa int pq pode ser numero não inteiro, ex: 5.5 , 7.5
n2 = float(input("Digite a nota da PROVA 2:"))
nf= n1+n2
media= nf//2
# m = ( n1+n2) /2 outro modo de se fazer o mesmo das linhas 4 e 5.
print("A nota da PROVA 1 é {} e da PROVA 2 é {}, a média final vale {}" .format(n1,n2,media))