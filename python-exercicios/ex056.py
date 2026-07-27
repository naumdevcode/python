cadastro = []
soma_idades = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
total_mulheres_jovens = 0
for c in range(1, 5):
    print(f"--- {c}ª PESSOA ---")
    pessoa = {  # Criamos o dicionário primeiro
        'nome': str(input('Seu nome: ')).strip().title(),
        'idade': int(input('Sua idade: ')),
        'sexo': str(input('Seu sexo [M/F]: ')).strip().upper()[0]
    }
    cadastro.append(pessoa) # Adicionamos na lista
    soma_idades += pessoa['idade']  # Processamento dos dados usando a variável 'pessoa'
    if pessoa['sexo'] == 'M' and pessoa['idade'] > maior_idade_homem:
        maior_idade_homem = pessoa['idade']
        nome_homem_mais_velho = pessoa['nome']
    if pessoa['sexo'] == 'F' and pessoa['idade'] < 20:
        total_mulheres_jovens += 1
media_idades = soma_idades / len(cadastro)
print('\n' + '='*40)
print(f'A média de idade do grupo é {media_idades:.1f} anos.')
if nome_homem_mais_velho:   # Tratamento para o caso de não haver homens cadastrados
    print(f'O homem mais velho é {nome_homem_mais_velho} com {maior_idade_homem} anos.')
else:
    print('Não foi cadastrado nenhum homem no grupo.')

print(f'Ao todo temos {total_mulheres_jovens} mulher(es) com menos de 20 anos.')