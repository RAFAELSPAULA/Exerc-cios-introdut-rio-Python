# Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
# nomes e a idade média entre essas pessoas, com uma casa decimal, conforme exemplo.

# Recebendo informações da primeira pessoa

print('Dados da primeira pessoa:')
Nome1 = str(input('Nome:'))
Idade1 = int(input('Idade:'))

# Recebendo informações da segunda pessoa

print('Dados da segunda pessoa:')
Nome2 = str(input('Nome:'))
Idade2 = int(input('Idade:'))

# Cálculo da média de idades

media = (Idade1 + Idade2) / 2

# Imprimir o resultado

print('A idade média de', Nome1, 'e', Nome2, 'é de', media, 'anos'.format(media=media))

