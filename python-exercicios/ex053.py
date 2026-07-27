frase = str(input('Digite uma frase: ')).strip().lower().split()
frase = ''.join(frase)
n = len(frase)
pfrase = ''
for c in range(n-1,-1,-1):
    pfrase += frase[c]
if frase == pfrase:
    print(f'Essa frase é um palidromo, {pfrase}')
else:
    print(f'Essa frase não é um palidromo')