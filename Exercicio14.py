# 14. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
# mensagem caso o valor seja inválido e continue pedindo até que o usuário
# informe um valor válido.


for x in range(11,1001):
    nota = int(input("Informe uma nota entre 0 e 10: "))    
    if nota >=0 and nota <= 10:
        print("Valor válido")
        break
        print("Valor inválido")
        