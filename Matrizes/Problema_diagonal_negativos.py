# Fazer um programa para ler um número inteiro N (máximo = 10) e uma matriz quadrada de ordem N
# contendo números inteiros. Em seguida, mostrar a diagonal principal e a quantidade de valores
# negativos da matriz.

n = int(input('Qual a ordem da matriz?'))

mat : [[int]] = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("DIAGONAL PRINCIPAL:")

for i in range(n):
	print(f"{mat[i][i]} ", end="")

neg = 0

for i in range(n):
    for j in range(n):
        if mat[i][j] < 0:
            neg = neg + 1

print(f"\nQUANTIDADE DE NEGATIVOS = {neg}")