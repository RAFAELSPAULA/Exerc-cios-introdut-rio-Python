# Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três
# números lidos. Em caso de empate, mostrar apenas uma vez.

# Inserindo Valores

A = int(input('Primeiro valor: '))
B = int(input('Primeiro valor: '))
C = int(input('Terceiro valor: '))

# Estabelecendo condição para apresentar Menor número digitado

if (A < B) and (A < C):
    print('MENOR: ', A)
elif (B < C):
    print('MENOR: ', B)
else:
    print('MENOR: ', C)

