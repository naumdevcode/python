import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
# hi = math.sqrt(math.pow(co,2)+math.pow(ca,2))
hi = math.hypot(co, ca)
print('A hipotenusa desse triângulo é {:.2f}'.format(hi))