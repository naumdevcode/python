from datetime import datetime
ano = int(input('Seu ano de nascimento: '))
idade = datetime.now().year - ano
def categoria(id):
    if id < 10:
        return 'MIRIM'
    elif id < 15:
        return 'INFANTIL'
    elif id < 20:
        return 'JUNIOR'
    elif id < 21:
        return 'SÊNIOR'
    else:
        return 'MASTER'
print()
print(f'Você tem {idade} anos, sua categoria é {categoria(idade)}')