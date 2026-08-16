sexo = ''
while sexo not in 'MF' or sexo == '':
    sexo = str(input('Qual o seu sexo [M/F]: ')).strip().upper()[0]
    if sexo not in 'MF' or sexo == '':
        print('Sexo inválido, tente novamente')
print(f'Sexo {sexo} registrado com sucesso!')