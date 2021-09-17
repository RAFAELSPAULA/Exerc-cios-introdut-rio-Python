# Fazer um programa para ler dois valores inteiros X e Y, e depois mostrar na tela o valor da soma destes
# números.

# Usuário inserido valor de x e y

x = int(input('Digite o valor de X:'))
y = int(input('Digite o valor de Y:'))

# Cálculo dos valores inseridos

soma = x + y

#Imprimindo resultado

resultado = 'Soma: {soma}'.format(soma=soma)

print(resultado)