# Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa
# que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número
# de homens.

n = int(input('Quantas pessoas serao digitadas? '))

altura : [float] = [0 for x in range(n)]
genero : [str] = [0 for x in range(n)]

Menor = 3
Maior = 0
SomaM = 0
base = 0
H = 0

for i in range(0,n):
    altura[i] = float(input(f'Altura da {i+1}a pessoa:'))
    genero[i] = str(input(f'Genero da {i+1}a pessoa:'))

for i in range(0,n):
    if altura[i] < Menor:
        Menor = altura[i]
    elif altura[i] > Maior:
        Maior = altura[i]

for i in range(0,n):
    if genero[i] == 'F':
        SomaM = SomaM + altura[i]
        base = base + 1
        media = SomaM / base
    elif genero[i] == 'M':
        H = H + 1

print(f'Menor altura = {Menor:.2f}'
      f'\nMaior altura = {Maior:.2f}'
      f'\nMedia das alturas das mulheres = {media:.2f}'
      f'\nNumero de homens = {H}')


