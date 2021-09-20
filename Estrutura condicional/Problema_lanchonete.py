# Uma lanchonete possui vários produtos. Cada produto possui um código  e um preço. Você deve fazer um programa para ler o código e a
# quantidade comprada de um produto (suponha um código válido), e daí informar qual o valor a ser pago, com duas casas decimais, conforme
# tabela de produtos.

# Código do produto  e Preço do produto

# 1 = R$ 5.00
# 2 = R$ 3.50
# 3 = R$ 4.80
# 4 = R$ 8.90
# 5 = R$ 7.32

# Inserindo Valores

Codigo = float(input('Codigo do produto comprado: '))
Quantidade = int(input('Quantidade comprada: '))

# Inserindo valor a variável Pagar

pagar = 0

# Estabelecendo condição para produto selecionado e valor devido de acordo com quantidade e produto selecionado.

if Codigo == 1:
    pagar = Quantidade * 5.00
elif Codigo == 2:
    pagar = Quantidade * 3.50
elif Codigo == 3:
    pagar = Quantidade * 4.80
elif Codigo == 4:
    pagar = Quantidade * 8.90
elif Codigo == 5:
    pagar = Quantidade * 7.32

print(f'Valor a pagar: R$ {pagar:.2f}')






