amount_money_carteira = float(input('Quanto tenho na carteira? R$'))
price_dolar_actualy = 4
convert_dolar = amount_money_carteira / price_dolar_actualy

print('Com R${:.2f} você pode comprar U${:.2f}'.format(amount_money_carteira, convert_dolar))