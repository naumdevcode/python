r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
def isTriangulo():
    if (r1 + r2 > r3) and (r2 + r3 > r1) and (r3 + r1 > r2):
        return True
    else:
        return False
def formTriangulo():
    if r1 == r2 == r3:
        return 'EQUILÁTERO'
    elif (r1 == r2) or (r2 == r3) or (r3 == r1):
        return 'ISÓSCELES'
    else:
        return 'ESCALENO'
if isTriangulo():
    print(f'Os segmentos acima PODEM FORMAR um triângulo {formTriangulo()}.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo.')