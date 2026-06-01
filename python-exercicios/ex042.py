r1 = float(input('Digite o tamanho da uma reta: '))
r2 = float(input('Digite o tamanho de outra reta: '))
r3 = float(input('Digite o tamanho de mais outra reta: '))
print()
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
    print(f'Isso é um triangulo {formTriangulo()}.')
else:
    print('Isso não é um tringulo.')