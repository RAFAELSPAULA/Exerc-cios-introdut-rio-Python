# Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de
# senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha
# for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
# encerrado. Considere que a senha correta é o valor 2002.

# Informação para usuário

print('Digite a senha:')

# Inserindo valores

senha = int(input())

# Condições para senha ser validada

while senha != 2002:

    print('Senha Invalida! Tente novamente:')
    senha = int(input())

    if senha == 2002:
        print('Acesso permitido! ')