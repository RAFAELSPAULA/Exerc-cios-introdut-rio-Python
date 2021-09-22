# Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma
# mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O
# programa deve finalizar quando forem digitados dois valores iguais.

# Informação para usuário

print('Digite dois numeros: ')

# Inserindo Valores

N1 = int(input())
N2 = int(input())

# Condição de repetição até que seja digitado uma combinação nula

while N1 != N2:
    if N1 < N2:
        print('CRESCENTE')
    else:
        print('DECRESCENTE')

    print('Digite outros dois numeros: ')

    N1 = int(input())
    N2 = int(input())