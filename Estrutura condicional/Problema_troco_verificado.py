# Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
# O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
# e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
# ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
# valor restante.

# Inserindo Valores

PrecoU = float(input('Preço unitário do produto: '))
Quantidade = int(input('Quantidade comprada: '))
DinheiroR = float(input('Dinheiro recebido: '))

# Cálculo dos Valores

ValorF = DinheiroR -  PrecoU * Quantidade

# Estabelecendo condições do troco

if ValorF > 0:
    print(f'TROCO: {ValorF:.2f}')
else:
    print(f'DINHEIRO INSUFICIENTE. FALTAM {ValorF:.2f} Reais')