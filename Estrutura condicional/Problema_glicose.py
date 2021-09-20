# Fazer um programa para ler a quantidade de glicose  no sangue de uma pessoa e depois mostrar na tela a
# classificação desta glicose de acordo com a tabela de referência.

# Classificação Glicose
# Normal Até 100 mg/dl
# Elevado Maior que 100 até 140 mg/dl
# Diabetes Maior de 140 mg/dl

# Inserindo Valores

Glicose = float(input('Digite a medida da glicose: '))

# Estabelecendo condições para identificar tabela com valor inserido pelo usuário.

if Glicose < 100 or Glicose == 100:
 print('Normal')
elif Glicose > 100 and Glicose < 140 or Glicose == 140:
 print('Elevado')
else:
 print('Diabetes')
