# Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo
# segundo. Caso não for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”.

x = int(input('Quantos casos voce vai digitar?'))

for i in range(0,x):
    a = float(input('Entre com o numerador:'))
    b = float(input('Entre com o numerador:'))
    if b == 0:
        print('Divisão Impossível')
    else:
        divisao = a / b
        print(f'DIVISAO = {divisao:.2f}')
