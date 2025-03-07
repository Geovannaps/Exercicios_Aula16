# 2. Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

num = int(input("Digite um número: "))
num1 = int(input("Digite outro número :"))

for i in range(num+1, num1, 1):
    print(i)