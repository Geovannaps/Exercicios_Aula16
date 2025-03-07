# # 13. Faça um programa que peça 10 números inteiros, calcule e mostre a
# quantidade de números pares e a quantidade de números impares.

cont_par = 0
cont_impar = 0

for i in range(10):
    num = int(input(f"{i+1})Informe o um número: "))
    if num%2 == 0:
        cont_par +=1
    else:
        cont_impar +=1
print(f"Números pares = {cont_par}")
print(f"Números impares = {cont_impar}")
