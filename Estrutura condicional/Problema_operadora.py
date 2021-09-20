# Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de
# telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para
# ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.

# Inserindo Valor

TEMPO = int(input('Digite a quantidade de minutos: '))

# Valor Fixo

VALOR = 50.00

# Estabelecendo condição de tempo para ver se a valor adicional a ser pago

if TEMPO < 100 or TEMPO == 100:
    print(f'Valor a pagar: R$ {VALOR:.2f}')
else:
    Adicional = ((TEMPO - 100) * 2.0) + VALOR
    print(f'Valor a pagar: R$ {Adicional:.2f}')
