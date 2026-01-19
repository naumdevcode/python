a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
area = a*l
lt = area/2
print('A parede tem {:.2f}m², precisará de {:.2f}L de tinta para pintar'.format(area,lt))