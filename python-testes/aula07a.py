n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {} \no produto é {} \na divisão é {:.3f}'.format(s,m,d), end=' ===> ')
print('a divisão inteira {} \na potencia {}'.format(di,e))