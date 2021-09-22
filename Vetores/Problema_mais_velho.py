# Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes
# devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome
# da pessoa mais velha.

n = int(input('Quantas pessoas voce vai digitar? '))

vetN : [str] = [0 for x in range(n)]
vetI : [int] = [0 for x in range(n)]

velho = 0

for i in range(0,n):
    print(f'Dados da {i+1}a pessoa: ')
    vetN[i] = str(input('Nome: '))
    vetI[i] = int(input('Idade: '))
    if vetI[i] > velho:
        velho = vetI[i]
        posi = i

print(f'PESSOA MAIS VELHA: {vetN[posi]}')


