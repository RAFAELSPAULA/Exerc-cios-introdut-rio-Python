# Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para
# isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser
# informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com
# duas casas decimais. A seguir é dada a fórmula para converter de Fahrenheit para Celsius (você deve
# deduzir a fórmula de Celsius para Fahrenheit): C = 5/9(F-32)

# Usuário escolhendo qual temperatura começar.

Temp = str(input('Voce vai digitar a temperatura em qual escala (C/F)?'))

# Determinando condições para conversão e fórmulas.

if Temp == 'F':
    F = float(input(f'Digite a temperatura em Fahrenheit: '))
    Cc = (F-32) / 1.8
    print(f'Temperatura equivalente em Celsius: {Cc:.2f}')
elif Temp == 'C':
    C = 0
    C = float(input(f'Temperatura equivalente em Celsius: '))
    Ff = C * 1.8 + 32
    print(f'Temperatura equivalente em Fahrenheit: {Ff:.2f}')
else:
    print('Temperatura digitada não condiz com as possibilidades')

