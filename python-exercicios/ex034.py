sal = float(input('Quanto é o seu salário: '))
if sal > 1250:
    new = sal + (sal*0.1)
    p = 10
else:
    new = sal + (sal*0.15)
    p = 15
print('O seu salário de R${:.2f} com aumento de {}%, fica R${:.2f}'.format(sal,p,new))