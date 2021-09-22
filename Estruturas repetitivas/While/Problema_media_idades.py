# Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um
# indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular
# e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez,
# mostrar a mensagem "IMPOSSIVEL CALCULAR".

# Inserindo Informações

print('Digite as idades: ')

# Inserindo Valores

Idade = int(input())

# Dando Valor as Variáveis

somaI = 0
base = 1

# Condição para executar

while Idade > 0:
    somaI = somaI + Idade
    Idade = int(input())
    if Idade > 0:
        base = base + 1
Media = somaI / base

if somaI > 0:
    print(f'Média : {Media:.2f}')
else:
    print('Impossivel calcular')











