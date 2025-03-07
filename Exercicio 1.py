# 1. Faça um programa que leia 5 números e informe o maior número.
contador = 0

for i in range(1,6):
    num = int(input("Informe um número: "))
    if num > contador:
        contador = num
print(f"O maior número é {contador}")