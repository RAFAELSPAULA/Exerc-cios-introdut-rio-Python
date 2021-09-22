# Leia um valor inteiro X. Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X,
# se for o caso.

# Inserindo valor da variável

x = int(input('Digite o valor de X:'))

# Condição de repetição

for i in range(x):
    if i % 2 != 0:
        print(i)