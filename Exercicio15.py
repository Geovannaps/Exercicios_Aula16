# 15. Uma loja tem tem uma política de descontos de acordo com o valor da
# compra do cliente. Os descontos começam acima dos R$500. A cada 100
# reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até
# 25%.

# valor_compra = 0
# desconto = 0
# valor_final = 0

# valor_compra = float(input("Informe o valor da compra: "))

# if valor_compra > 500:
#     desconto = (valor_compra - 500) // 100
#     if desconto > 25:
#         desconto = 25
#     valor_final = valor_compra - (valor_compra*(desconto/100))
#     print(f"Valor da compra = {valor_compra} - Desconto = {desconto}% - Valor final {valor_final}")

# else:
#     print("Não possui desconto")

for valor in range(500,3100,100):
    desconto = min((valor - 500) // 100 + 1, 25)
    valor_final = valor - (valor *(desconto / 100))
    print(f"O valor da compra é {valor}, o valor do desconto é {desconto} e o valor final é {valor_final}")