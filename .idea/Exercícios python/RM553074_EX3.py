notas_pares = []
notas_impares = []

for n_aluno in range(1, 51):
    nota = -1
    while nota < 0 or nota > 10:
        nota = float(input(f"Por favor, insira a nota do aluno número {n_aluno}: "))
    if n_aluno % 2 == 0:
        notas_pares.append(nota)
        print("Você está digitando as notas dos alunos pares")
    else:
        notas_impares.append(nota)
        print("Você está digitando as notas dos alunos ímpares")

total_pares = 0
total_impares = 0
media_pares = 0
media_impares = 0

if notas_pares:
    total_pares = sum(notas_pares)
    media_pares = total_pares / 25
    print("A média de nota dos números pares é de {:.2f}".format(media_pares))

if notas_impares:
    total_impares = sum(notas_impares)
    media_impares = total_impares / 25
    print("A média de nota dos números impares é de {:.2f}".format(media_impares))

if media_pares > media_impares:
    print("Os números pares têm a maior média")
elif media_impares > media_pares:
    print("Os números ímpares têm a maior média")
else:
    print("A média de ímpares e pares é igual, houve um empate")

#ELABORADO POR: BRUNA MENDES DA CUNHA PASSOS RM:553074







