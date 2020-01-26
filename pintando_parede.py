largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area/2
print('sua parede tem as dimensões {} x {} e a sua área é {}m²'.format(largura,altura,area))
print('para pintar sua parede, você precisa de {} litros de tinta'.format(tinta))
