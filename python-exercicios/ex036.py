cores = {'bold': '\033[1m',
         'invert': '\033[7m',
         'clean': '\033[m',
         'vemelho': '\033[1;41m',
         'verde': '\033[1;42m'}

casa = float(input(f'{cores['bold']}Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

print(f'{cores['clean']}')

Qparc = int(anos*12)
prestacao = float(casa/Qparc)
max = float(salario*0.3)
credito = max*Qparc

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end='')
print(f' a prestação será de R${prestacao:.2f}')

if prestacao <= max:
    print(f'{cores['verde']}{"Empréstimo pode ser CONCEDIDO!".center( 50, "=")}{cores['clean']}')
else:
    print(f'{cores['vemelho']}{"Empréstimo NEGADO!".center(50, "=")}{cores['clean']}')
    print(f'Crédito liberado: {credito:.2f}')
    