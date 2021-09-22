# Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
# Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma:
# 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a
# 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o
# código informado for o número 4, devendo então mostrar a mensagem "MUITO OBRIGADO", bem
# como as quantidades de cada combustível.

# Fornecendo Valores as Variáveis

x = 0
A = 0
G = 0
D = 0

# Condição com soma de itens.

while x != 4:
    x = int(input('Informe um codigo (1, 2, 3) ou 4 para parar: '))
    if x == 1:
        A = A + 1
    elif x == 2:
        G = G + 1
    elif x ==3:
        D = D + 1

# Imprimindo resultado

print(f'Álcool: {A}'
      f'\nGasolina: {G}'
      f'\nDiesel: {D}'
      '\nMUITO OBRIGADO')
