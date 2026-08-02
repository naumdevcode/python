frase_original = str(input('Digite uma frase: ')).strip().upper()
frase_junta = ''.join(frase_original.split())
frase_contrario = frase_junta[::-1]
'''frase_contrario = ''
for c in range(len(frase_junta)-1,-1,-1):
    frase_contrario += frase_junta[c]'''
print(F'O inverso de {frase_original} é {frase_contrario}')
if frase_junta == frase_contrario:
    print(f'Temos um palidromo!')
else:
    print(f'A frase digitada não é um palidromo!')