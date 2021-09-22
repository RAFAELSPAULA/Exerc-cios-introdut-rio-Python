# Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10

# Inserindo valor de X

x = int(input('Deseja a tabuada para qual valor? '))

# Para de elemento i que vai de 1 até 10 (sempre considerar 1 a mais)
# Fazemos o produto de x * i e imprimimos o resultado

for i in range(1,11):
    produto = x * i
    print(f'{x} x {i} = {produto}')