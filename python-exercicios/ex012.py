p = float(input('O valor do produto: R$'))
d = p-(p*5/100)
pa = (p+(p*8/100))/10
print('O produto de R${} pagando avista, ganha 5% de deconto e fica por R${:.2f}'.format(p,d))
print('Parcelado fica 10X de R${}'.format(pa))