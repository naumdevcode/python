from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
def categoria(id):
    if id <= 9:
        return 'MIRIM'
    elif id <= 14:
        return 'INFANTIL'
    elif id <= 19:
        return 'JUNIOR'
    elif id <= 25:
        return 'SÊNIOR'
    else:
        return 'MASTER'
print(f'O atleta tem {idade} anos.')
print(f'Classificação: {categoria(idade)}')