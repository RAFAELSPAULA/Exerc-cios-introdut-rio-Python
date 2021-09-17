# Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
# casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
# o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos
# com duas casas decimais.


# Primeiro momento usuário informa os dados abaixo:

largura = float(input('Digite a largura do terreno: '))

comprimento = float(input('Digite o comprimento do terreno: '))

metro_quadrado = float(input('Digite o valor do metro quadrado:'))

# Em seguida realizamos as operações para ter os valores do Terreno

area = largura * comprimento

preco = area * metro_quadrado

# Por fim apresentamos o resultado

# Colocando resultado usando .format  para não precisar concatenar uma a uma, e para fazer entendamento do .format foi usado Enter
#:.2f e para decidir quantidade de casa decimal, após a vírgula

resultado = ('largura: {largura}'
             '\ncomprimento:  {comprimento}'
             '\nmetro_quadrado: {metro_quadrado}'
             '\narea: {area:.2f}'
             '\npreco: {preco:.2f}'.format(largura=largura,
                                       comprimento=comprimento,
                                       metro_quadrado=metro_quadrado,
                                       area=area,
                                       preco=preco))
print(resultado)

