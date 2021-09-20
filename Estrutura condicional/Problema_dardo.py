# No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir.
# Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual
# foi a maior.

# Informação do usuário

print('Digite as tres distancias:')

# Inserindo Valores

A = float(input())
B = float(input())
C = float(input())

# Estabelecendo condição para determinar maior valor

if (A > B) and (A > C):
    print(f'MAIOR DISTANCIA = {A:.2f}')
elif B > C:
    print(f'MAIOR DISTANCIA = {B:.2f}')
else:
    print(f'MAIOR DISTANCIA = {C:.2f}')
