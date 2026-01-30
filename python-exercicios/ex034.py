sal = float(input('Quanto é o salário do funcionário: R$'))
if sal > 1250:
    new = sal *1.1
    p = 10
else:
    new = sal * 1.15
    p = 15
print('O seu salário de R${:.2f} com aumento de {}%, fica R${:.2f}'.format(sal,p,new))