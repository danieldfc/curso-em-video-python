largura,altura = map(float, input('Largura e altura: ').split())

area = largura * altura
litros_tinta = area / 2

print('Sua parede tem dimensão de {}x{} e sua área é de {:.3f}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.4f}l de tinta.'.format(litros_tinta))
