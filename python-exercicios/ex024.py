cid = input('Digite o nome de uma cidade: ')
div = cid.lower().split()
print('Essa cidade começa com "SANTO": {}'.format('santo' in div[0]))