# Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
# combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo
# médio do carro, com três casas decimais.

# Inserindo Valores

DistanciaP = float(input('Distancia percorrida:'))
CombustivelG = float(input('Distancia percorrida:'))

# Cálculando Valores

ConsumoM = DistanciaP / CombustivelG

# Imprimir Valores

Resultado = f'Consumo medio = {ConsumoM:.3f}'.format(ConsumoM=ConsumoM)

print(Resultado)