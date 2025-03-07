# 10. Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja A
# foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse
# valor mostre na tela uma mensagem contendo em quanto foi superado o
# faturamento.

faturamento = 0
loja_B = 54000

for loja_A in range(5):
    valor_gasto = float(input("Quanto você gastou na loja?"))
    faturamento += valor_gasto
if faturamento > loja_B:
    diferenca = faturamento - loja_B 
    print(f"O valor foi superado em R${diferenca}")
else:
    print("O valor gasto não atingiu o faturamento da loja B")