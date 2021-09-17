# Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
# O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
# e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
# mostrar o valor do troco a ser devolvido ao cliente.

# Inserindo valores conforme usuário deseja

Preco = float(input('Preço unitário do produto:'))
Quantidade = int(input('Preço unitário do produto:'))
Dinheiro = float(input('Dinheiro recebido:'))

# Cálculando valores

troco = (Dinheiro - (Preco * Quantidade))

# Imprimindo Resultado

resultado = f'TROCO {troco:.2f}'.format(troco=troco)

print(resultado)
