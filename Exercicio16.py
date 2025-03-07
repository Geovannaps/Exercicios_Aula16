# 16. Faça um programa que receba a idade de 15 pessoas e que calcule e
# mostre:

crianca = 0
adolecente = 0
adulto = 0
meia_idade = 0
idoso = 0

for i in range(1,16):
    idade = int(input("Informe a idade: "))
    if idade <= 15:
        crianca += 1
    elif idade >= 16 and idade <= 30:
        adolecente += 1
    elif idade >= 31 and idade <= 45:
        adulto += 1
    elif idade >= 46 and idade <= 60:
        meia_idade += 1
    elif idade > 61:
        idoso += 1
    else:
        print()

total_pessoas = 15

print(f"A quantidade de crianças é: {crianca}, representando {(crianca/total_pessoas)*100}%")
print(f"A quantidade de adolecentes é: {adolecente}")
print(f"A quantidade de adultos é: {adulto}")
print(f"A quantidade de pessoas de meia idade é: {meia_idade}")
print(f"A quantidade de idosos é: {idoso}, representando {(adulto/total_pessoas)*100}%")