# Fazer um programa para ler dois números inteiros M e N (máximo = 10). Em seguida, ler uma matriz
# de M linhas e N colunas contendo números reais. Gerar um vetor de modo que cada elemento do vetor
# seja a soma dos elementos da linha correspondente da matriz. Mostrar o vetor gerado.

m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))

matriz: [[float]] = [[0 for x in range(n)] for x in range(m)]
vetor: [float] = [0 for x in range(m)]

for i in range(m):
	print(f"Digite os elementos da {i + 1} a. linha")
	for j in range(n):
		matriz[i][j] = float(input())

for i in range(m):
	somalinha = 0

	for j in range(n):
		somalinha = somalinha + matriz[i][j]
	vetor[i] = somalinha

print("VETOR GERADO:")

for i in range(m):
	print(f"{vetor[i]:.1f}")