# # 9. Faça um programa que peça um número inteiro e determine se ele é ou
# não um número primo. Um número primo é aquele que é divisível somente
# por ele mesmo e por 1.

num = int(input("Informe um número inteiro: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Número não é primo")
            break
    else:
        print("Número primo")
