num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidades: {} \ndezenas: {} \ncentenas: {} \nmilhares: {}'.format(u,d,c,m))