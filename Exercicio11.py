# 11. Faça um programa que peça para n pessoas a sua idade, ao final o
# programa deverá verificar se a média de idade da turma varia entre 0 e
# 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou
# idosa, conforme a média calculada.

n = int(input("Informe o número de pessoas: "))
soma = 0

for x in range(n):
    idade = int(input(f"Digite a idade da pessoa {x+1}:"))
    soma += idade
    media = soma/2
if media > 0 and media <= 26:
    print("Jovem")
elif media > 26 and media <= 60:
    print("Adulto")
elif media > 60:
    print("Idoso")
    