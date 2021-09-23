# Ler um inteiro N (máximo = 10) e uma matriz quadrada de ordem N contendo números inteiros. Mostrar a soma dos elementos acima da
# diagonal principal. Um exemplo de números acima da diagonal principal.

n = int(input('Qual a ordem da matriz?'))

mat : [[int]] = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

soma = 0

for i in range(n):
    for j in range(n):
        if i < j:
            soma = soma + mat[i][j]

print(f"SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {soma}")