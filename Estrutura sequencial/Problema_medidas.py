# Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
# com quatro casas decimais):
# a) a área do quadrado que tem lado A
# b) a área do triângulo retângulo que base A e altura B
# c) a área do trapézio que tem bases A e B, e altura C

# Inserindo Valores

A = float(input('Digite a medida A:'))
B = float(input('Digite a medida B:'))
C = float(input('Digite a medida C:'))

# Cálculando Valores

AreaQ = A * 4
AreaT = (A * B) / 2
AreaTR = ((A + B) * C) / 2

# Imprimindo Resultado

Resultado = (f'AREA DO QUADRADO = {AreaQ:.4f}'
            f'\nAREA DO TRIANGULO = {AreaT:.4f}'
            f'\nAREA DO TRIANGULO = {AreaTR:.4f}'.format(AreaQ=AreaQ,
                                                         AreaT=AreaT,
                                                         AreaTR=AreaTR))
print(Resultado)