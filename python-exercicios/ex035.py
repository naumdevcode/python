r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if (r1 + r2 > r3) & (r2 + r3 > r1) & (r3 + r1 > r2):
    print('O tamanho dessas reta podem formar um triângulo')
else:
    print('O tamanho dessas reta NÃO podem formar um triângulo')