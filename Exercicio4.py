# 4. Faça um programa que leia 5 números e informe a soma e a média dos
# números.

contador_soma = 0

for i in range(1,6):
    num = int(input("Informe um número: "))
    contador_soma += num
    media = contador_soma/i
print(f"A soma dos números é {contador_soma} e a média {media}")
