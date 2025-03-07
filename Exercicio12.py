# 12. Numa eleição existem três candidatos. Faça um programa que peça o
# número total de eleitores. Peça para cada eleitor votar e ao final mostrar o
# número de votos de cada candidato.

contador1 = 0
contador2 = 0
contador3 = 0

total_eleitores = int(input("Informe o total de eleitores:"))

for i in range(total_eleitores):
    candidato = int(input("Informe seu voto(10,20,30): "))
    if candidato == 10:
        contador1 += 1
    elif candidato == 20:
        contador2 += 1
    elif candidato == 30:
        contador3 += 1
print(f"Candidato 1 = {contador1} votos")
print(f"Candidato 2 = {contador2} votos")
print(f"Candidato 3 = {contador3} votos ")