cores = {'vermelho' : '\033[1;41m',
         'amarelo' : '\033[1;43m',
         'verde' : '\033[1;42m',
         'limpar' : '\033[m'}
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
print()
media = (nota1+nota2)/2
print(f'Sua média: {media:.1f}')
if media < 5:
    print(f'Você está {cores["vermelho"]}REPROVADO{cores["limpar"]}')
elif media < 7:
    print(f'Você está de {cores["amarelo"]}RECUPERAÇÃO{cores["limpar"]}')
else:
    print(f'Você está {cores["verde"]}APROVADO{cores["limpar"]}')