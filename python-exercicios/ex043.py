altura = float(input('Sua altura (m): '))
peso = float(input('Seu peso (kg): '))
print()
def imc(i):
    if i < 18.5:
        return 'Abaixo do peso'
    elif i < 25:
        return 'Peso ideal'
    elif i < 30:
        return 'Sobrepeso'
    elif i < 40:
        return 'Obesidade'
    else:
        return 'Obesidade mórbida'
indice = peso / (altura**2)
print(f'Seu IMC: {indice:.1f}, {imc(indice)}')