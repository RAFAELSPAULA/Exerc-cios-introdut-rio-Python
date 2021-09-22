# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a
# média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao
# intervalo [0,10]). Cada nota deve ser validada separadamente.

# Inserindo Primeiro Valor

x1 = float(input('Digite a primeira nota: '))

# Primeira Condição

while x1 < 0 or x1 > 10:
    print('Valor invalido! Tente novamente:')
    x1 = float(input('Digite a primeira nota: '))

# Inserindo Segundo Valor

x2 = float(input('Digite a segunda nota: '))

# Segunda Condição

while x2 < 0 or x2 > 10:
    print('Valor invalido! Tente novamente:')
    x2 = float(input('Digite a segunda nota: '))

# Cálculando Valores e dando valores a variáveis e por fim imprimindo valor.

base = 0

if x1 > 0:
    base  = base + 1

if x2 > 0:
    base = base + 1

Media = (x1 + x2) / base

print(f'Media = {Media:.2f}')


