import math
ang = float(input('Digite um angulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O seno é {:.2f} \nO cosseno é {:.2f} \nE a tangente é {:.2f}'.format(seno, cos, tang))