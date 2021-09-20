# Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
# de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais,
# conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem.

# Importando o Módulo Math para usar raiz quadrada.

import math

# Inserindo Valores

A = float(input('Coeficiente a: '))
B = float(input('Coeficiente b: '))
C = float(input('Coeficiente c: '))

# Calculando Valores

Delta = B ** 2.0 - 4.0 * A * C

# Imprimir Resultado e caso delta < 0 fazer cálculo do x1 e x2 

if Delta < 0:
    input('Esta equacao nao possui raizes reais')
else:
    x1 = (-B + math.sqrt(Delta)) / (2.0 * A)
    x2 = (-B - math.sqrt(Delta)) / (2.0 * A)

# Ajustando casas decimais e concatenando str com float para apresentar no resultado.

    Resultado = (f'X1 {x1:.4f},'
                 f'\nX2 {x2:.4f}'.format(x1=x1,
                                         x2=x2))
    input(Resultado)


