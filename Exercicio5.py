# 5. Faça um programa que receba um número e usando laços de repetição
# calcule e mostre a tabuada desse número.

num = int(input("Informe um número: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

