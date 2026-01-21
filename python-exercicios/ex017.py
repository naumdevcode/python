import math
co = int(input('Cateto oposto: '))
ca = int(input('Cateto adjacente: '))
h = math.sqrt(math.pow(co,2)+math.pow(ca,2))
print('A hipotenusa desse triângulo é {}'.format(h))