# Fazer um programa para ler o valor "r" do raio de um círculo, e depois mostrar o valor da área do
# círculo com três casas decimais. A fórmula da área do círculo é a seguinte: 𝑎𝑟𝑒𝑎 = 𝜋. 𝑟^2. Você pode
# usar o valor de 𝜋 fornecido pela biblioteca da sua linguagem de programação, ou então, se preferir, use
# diretamente o valor 3.14159.

# Importar Método Match para usar PI

import math

# Inserir o valor do raio

Raio = float(input('Digite o valor do raio do circulo:'))

# Cálculo da área

Area = math.pi * Raio ** 2

# Imprimindo Resultado

Resultado = f'Area = {Area:.3f}'.format(Area=Area)
print(Resultado)
