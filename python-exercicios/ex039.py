from datetime import datetime
nasc = int(input('Em que ano você nasceu? '))
print()

ano = datetime.now().year
idade = ano - nasc

if idade < 18:
    prazo = 18 - idade
    print(f'Você não precisa se alistar. Ainda faltam {prazo} anos.')
elif idade == 18:
    print('Você deve se alistar esse ano.')
else:
    prazo = idade - 18
    print(f'Você já passou {prazo} anos do tempo de se alistar.')