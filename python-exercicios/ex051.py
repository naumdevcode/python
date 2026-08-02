print(f"{' 10 TERMOS DE UMA PA '.center(40, '=')}")
num = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
for c in range(1,11):
    print(num,end=' → ')
    num += raz
print('ACABOU')