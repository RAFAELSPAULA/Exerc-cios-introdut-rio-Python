# Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
# tela todos os números pares, e também a quantidade de números pares.

n = int(input('Quantos numeros voce vai digitar? '))
vet: [int] = [0 for x in range(n)]

for i in range(0,n):
    vet[i] = int(input('Digite um numero: '))

print('\nNUMEROS PARES:')

for i in range(0,n):

    if vet[i] % 2 ==0:
        print(f'{vet[i]} ', end="")

Quantidade = 0

for i in range(-1,n):
    if i % 2 != 0:
        Quantidade = Quantidade + 1

print()
print(f'\nQUANTIDADE DE PARES {Quantidade}')
