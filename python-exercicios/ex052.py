cores = {
    'yellow' : '\033[1;33m',
    'clean' : '\033[m'
}
num = int(input('Digite um número: '))
tot = 0
for c in range(1,num+1):
    if c == 1:
        print('   0 ',end='')
    if c % 10 == 0:
        print()
    if num % c == 0:
        tot += 1
        print(cores['yellow'],f'{c:3}',cores['clean'],end='')
    else:
        print(f' {c:3} ',end='')
print()
print(f'O número {num} foi divisível {tot} vezes')
if tot == 2:
    print(f'E por isso ele É PRIMO!')
else:
    print(f'E por isso ele NÃO É PRIMO!')