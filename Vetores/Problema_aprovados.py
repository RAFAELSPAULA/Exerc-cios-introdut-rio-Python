# Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram
# no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em um vetor. Depois, imprimir
# os nomes dos alunos aprovados, considerando aprovados aqueles cuja média das notas seja maior ou
# igual a 6.0 (seis).

n = int(input('Quantos alunos serao digitados? '))

vetN : [str] = [0 for x in range(n)]
vetNo1 : [float] = [0 for x in range(n)]
vetNo2 : [float] = [0 for x in range(n)]
vetM : [float] = [0 for x in range(n)]

for i in range(0,n):
    print(f'Digite nome, primeira e segunda nota do {i+1}o aluno:')
    vetN[i] = str(input())
    vetNo1[i] = float(input())
    vetNo2[i] = float(input())
    vetM[i] = (vetNo1[i] + vetNo2[i]) / 2

print('Alunos aprovados: ')
for i in range(0,n):
    if vetM[i] >= 6:
        print(vetN[i])

