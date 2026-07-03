cores = {'vermelho' : '\033[1;41m',
         'amarelo' : '\033[1;43m',
         'verde' : '\033[1;42m',
         'limpar' : '\033[m'}
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2 ) / 2
print(f'tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
if media < 5:
    print(f'O aluno está {cores["vermelho"]}REPROVADO{cores["limpar"]}')
elif media < 7:
    print(f'O aluno está em {cores["amarelo"]}RECUPERAÇÃO{cores["limpar"]}')
else:
    print(f'O aluno está {cores["verde"]}APROVADO{cores["limpar"]}')