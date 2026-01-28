n = input('Digite seu nome: ').strip()
nome = n.split()
print('Seu primeiro nome: {} \nSeu ultimo nome: {}'.format(nome[0], nome[len(nome)-1]))