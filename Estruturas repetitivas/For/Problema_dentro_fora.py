# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo.

# Inserindo valor da variável x para quantidade de repetições

x = int(input('Quantos numeros voce vai digitar?'))

# Inserindo valores nas variáveis

dentro = 0
fora = 0

# Estrutura de repetição

for i in range(0,x):
    y = int(input('Digite um numero: '))
    if y >= 10 and y <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1

# Imprimindo valores

print(f'{dentro} Dentro'
      f'\n{fora} Fora')



