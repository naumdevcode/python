n = int(input('Digite um número: '))
d = 0
for c in range(1,n+1):
    if n % c == 0:
        d += 1
if d == 2 or n == 1:
    print(f'{n} é um número primo')
else:
    print(f'{n} não é um número primo')