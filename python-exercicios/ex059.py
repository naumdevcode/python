from time import sleep
menu = True
entradas = True
def pausa():
    print('-='*15)
    sleep(1.5)
while menu:
    while entradas:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        entradas = False
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''') 
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao  == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
        pausa()
    elif opcao == 2:
        print(f'O resultado de {n1} x {n2} é {n1*n2}')
        pausa()
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é o {maior}')
        pausa()
    elif opcao == 4:
        entradas = True
    elif opcao == 5:
        menu = False
        print('Finalizando...')
        pausa()
        print('Fim do programa! volte sempre!')
    else:
        print('Opção inválida. Tente novamente')
        pausa()
        