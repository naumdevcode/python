s = 0
for c in range(1,501):
    if c % 3 == 0 and c % 2 == 1:
        s += c
print(f'Essa é a soma entre todos os números ímpares que são multiplos de três que se encontram no intervalo de 1 até 500: {s}')