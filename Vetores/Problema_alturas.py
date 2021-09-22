# Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
# tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
# bem como os nomes dessas pessoas caso houver.

n = int(input('Quantas pessoas serao digitadas?'))
vetN: [str] = [0 for x in range(n)]
vetA: [float] = [0 for x in range(n)]
vetI: [int] = [0 for x in range(n)]

for i in range(0, n):
    print(f'Dados da {i+1}a pessoa:')
    vetN[i] = str(input('Nome: '))
    vetI[i] = int(input('Idade: '))
    vetA[i] = float(input('Altura: '))

somaA = 0

for i in range(0, n):
    somaA = somaA + vetA[i]

media = somaA / n
print(f'Altura média: {media:.2f}')

idadeM = 0
base = 0

for i in range(0, n):
    if vetI[i] < 16:
        idadeM = idadeM + 1


mediam = (idadeM / n) * 100
print(f'Pessoas com menos de 16 anos: {mediam:.1f}%')

for i in range(0, n):
    if vetI[i] < 16:
        print(vetN[i])











