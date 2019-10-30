price_product = float(input('Qual o preço do produto? R$'))
valor_desconto = 5
desconto = price_product - (price_product * (valor_desconto / 100))

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(price_product, desconto))