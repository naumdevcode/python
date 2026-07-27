from datetime import date
maior = 0
menor = 0
for c in range(1,8):
    nasc = int(input('Ano de nascimento: '))
    idade = date.today().year - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} são maiores de idade e {menor} são menores de idade.')