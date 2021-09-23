# Fazer um programa para ler duas matrizes de números inteiros A e B, contendo de M linhas e N colunas
# cada (M e N máximo = 10). Depois, gerar uma terceira matriz C onde cada elemento desta é a soma
# dos elementos correspondentes das matrizes originais. Imprimir na tela a matriz gerada

m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))

mat: [[int]] = [[0 for x in range(n)] for x in range(m)]
mat2: [[int]] = [[0 for x in range(n)] for x in range(m)]
mat3: [[int]] = [[0 for x in range(n)] for x in range(m)]

print("Digite os valores da matriz A:")

for i in range(m):
	for j in range(n):
		mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("Digite os valores da matriz B:")

for i in range(m):
	for j in range(n):
		mat2[i][j] = int(input(f"Elemento [{i},{j}]: "))

for i in range(m):
	for j in range(n):
		mat3[i][j] = mat[i][j] + mat2[i][j]

print("MATRIZ SOMA:")

for i in range(m):
	for j in range(n):
		print(f"{mat3[i][j]} ", end="")
	print()


