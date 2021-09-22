# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
# - Imprimir todos os elementos do vetor
# - Mostrar na tela a soma e a média dos elementos do vetor

N = int(input('Quantos numeros voce vai digitar?'))

vet : [float] = [0 for x in range(N)]

for i in range(0,N):
    vet[i] = float(input('Digite um numero:'))

print('\nVALORES = ', end='')

for i in range(0,N):
    print(f'{vet[i]:.1f} ', end="")

soma = 0

for i in range(0,N):
    soma = soma + vet[i]

print(f'\nSOMA = {soma:.2f}')

base = 0

for i in range(0,N):
    base = base + 1.0

media = soma / base
print(f'MEDIA = {media:.2f}')

