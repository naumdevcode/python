cores = {'bold': '\033[1m',
         'invert': '\033[7m',
         'clean': '\033[m',
         'vemelho': '\033[1;41m',
         'verde': '\033[1;42m'}

empr = float(input(f'{cores['bold']}Qual o valor do empréstimo? R$'))
anos = int(input('Em quantos anos você quer pagar? '))
sal = float(input('Quanto é o seu salário? R$'))

print(f'{cores['clean']}')

Qparc = int(anos*12)
Vparc = float(empr/Qparc)
Lsal = float(sal*0.3)
cred = Lsal*Qparc

if Vparc < Lsal:
    print(f'{cores['verde']}{"Seu empréstimo foi APROVADO".center( 50, "=")}{cores['clean']}')
    print(f'Valor do empréstimo: R${empr:.2f}')
    print(f'Parcelas de R${Vparc:.2f}/mês por {Qparc} meses')
    print(f'Seu salário: R${sal:.2f}')
else:
    print(f'{cores['vemelho']}{"Seu empréstimo foi NEGADO".center(50, "=")}{cores['clean']}')
    print(f'Valor do empréstimo muito alto para o seu salário')
    print(f'Crédito liberado: {cred:.2f}')
    