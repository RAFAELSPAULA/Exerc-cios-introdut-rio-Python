# Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida.
# Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também
# se é POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá imprimir apenas NULO.

x = int(input('Quantos numeros voce vai digitar?'))

for i in range(0,x):
    y = int(input('Digite um numero:'))
    if i % 2 == 0 and y > 0:
        print('Impar Positivo')
    elif i % 2 == 0 and y < 0:
        print('Impar Negativo')
    elif i % 2 != 0 and y > 0:
        print('Par Positivo')
    elif i % 2 != 0 and y < 0:
        print('Par Negativo')
    else:
        print('Nulo')
