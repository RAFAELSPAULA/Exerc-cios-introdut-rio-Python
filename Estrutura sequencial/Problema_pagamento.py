# Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
# quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com
# uma mensagem explicativa, conforme exemplo.

# Inserir Valores

Nome = str(input('Nome:'))
ValorH = float(input('Valor por Hora:'))
HorasT = float(input('Horas trabalhadas:'))

# Cálculo do Pagamento

Pagamento = ValorH * HorasT

# Imprimir Resultado

Resultado = f'{Pagamento:.2f}'.format(Pagamento=Pagamento)

print('O pagamento para', Nome, 'deve ser', Resultado)