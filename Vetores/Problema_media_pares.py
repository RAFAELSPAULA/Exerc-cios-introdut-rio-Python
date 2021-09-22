# Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na tela a média
# aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for
# digitado, mostrar a mensagem "NENHUM NUMERO PAR"

n = int(input('Quantos elementos vai ter o vetor? '))
vet : [float] = [0 for x in range(n)]

soma = 0
base = 0

for i in range(0,n):
    vet[i] = float(input('Digite um numero: '))
    if vet[i] % 2 == 0:
        soma = soma + vet[i]
        base = base +1
        media = soma / base

if base == 0:
    print('NENHUM NUMERO PAR')
else:
    print(f'MEDIA DOS PARES = {media:.1f}')

