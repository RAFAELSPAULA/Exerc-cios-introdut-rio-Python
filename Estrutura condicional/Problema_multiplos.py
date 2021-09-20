# Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro.
# Os números podem ser digitados em qualquer ordem.

# Imprimindo informação ao usuário

print('Digite dois numeros inteiros: ')

# Inserindo valores

N1 = int(input())
N2 = int(input())

# Estabelecendo condições para atender o caso.

if N1 % N2 == 0 or N2 % N1 == 0:
    print('São Multiplos')
else:
    print('Não São Multiplos')