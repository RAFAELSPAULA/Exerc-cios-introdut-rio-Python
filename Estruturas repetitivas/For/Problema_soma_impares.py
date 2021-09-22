# Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números
# impares entre eles.

# Informação para usuário

print('Digite dois números: ')

# Colocando valores para x e y

x = int(input())
y = int(input())

# Esse IF tem como finalidade armazena y e x e trocar de posição caso x seja maior que y;

if x > y:
    troca = x
    x = y
    y = troca

# Declarando valor a variável

soma = 0

# Repetição para realizar a soma

for i in range(x+1, y):
    if i % 2 != 0:
        soma = soma + i

# Imprimindo resultado

print(f'SOMA DOS IMPARES = {soma:.2f}')