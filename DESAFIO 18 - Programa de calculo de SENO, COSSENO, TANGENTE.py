#FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O CALOR DO SENO, COSSENO E TANGENTE DO ANGULO
import math
ângulo = float(input("Digite o angulo que voce deseja:"))
seno = math.sin(math.radians(ângulo))
print("O ângulo de {} tem o SENO de {:.2f}" .format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print(" O ângulo de {} tem COSSENO de {:.2f}" .format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print(" O ângulo de {} tem a TENGENTE de {:.2f}" .format(ângulo, tangente))
