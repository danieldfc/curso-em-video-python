numeric_value = int(input('Digite um número: '))

dobro = numeric_value * 2
triplo = numeric_value * 3
raiz_quadrada = numeric_value ** (1/2)

print('O dobro de {} vale {}.'.format(numeric_value, dobro))
print('O triplo de {} vale {}.'.format(numeric_value, triplo))
print('A raiz quadrada de {} vale {:.2f}.'.format(numeric_value, raiz_quadrada))