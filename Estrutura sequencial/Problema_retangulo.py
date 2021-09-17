# Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
# da área, perímetro e diagonal deste retângulo, com quatro casas decimais.


# Importanto método math para utilizar raiz quadrada

import math

# Inserir os valores.

base = float(input('Base do retangulo:\n'))
altura = float(input('Base do retangulo:\n'))

# Cálculo dos valores.

area = base * altura
perimetro = (2.0 * base) + (2.0 * altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

# Imprimir resultado.

resultado = ('base: {base}'
             '\naltura:  {altura}'
             '\narea: {area:.4f}'
             '\nperimetro: {perimetro:.4f}'
             '\ndiagonal: {diagonal:.4f}'.format(base=base,
                                       altura=altura,
                                       area=area,
                                       perimetro=perimetro,
                                       diagonal=diagonal))
print(resultado)



