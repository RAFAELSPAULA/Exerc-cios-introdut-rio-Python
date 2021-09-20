# Uma empresa vai conceder um aumento percentual de salário aos seus funcionários dependendo de quanto
# cada pessoa ganha, conforme tabela ao lado. Fazer um programa para ler o salário de uma pessoa, daí mostrar
# qual o novo salário desta pessoa depois do aumento, quanto foi o aumento e qual foi a porcentagem de aumento.

# Salário atual  e Aumento
# Até R$ 1000.00 - 20%
# Acima de R$ 1000.00 até R$ 3000.00 - 15%
# Acima de R$ 3000.00 até R$ 8000.00 - 10%
# Acima de R$ 8000.00 - 5%

# Inserindo Salário

Salario = float(input('Digite o salario da pessoa:'))

# Criando condição conforme tabela e cálculando os novos valores

if Salario < 1000 or Salario == 1000:
    Porcentagem = float(20/100)
    Aumento = Salario * Porcentagem
    NovoS = Salario + Aumento
    print(f'Novo salario = {NovoS:.2f}',
          f'\nAumento = {Aumento:.2f}',
          f'\nPorcentagem = {Porcentagem * 100}%'.format(NovoS=NovoS,
                                                   Aumento=Aumento,
                                                   Porcentagem=Porcentagem))
elif Salario > 1000 and Salario < 3000 or Salario == 3000:
    Porcentagem = float(15/100)
    Aumento = Salario * Porcentagem
    NovoS = Salario + Aumento
    print(f'Novo salario = {NovoS:.2f}',
          f'\nAumento = {Aumento:.2f}',
          f'\nPorcentagem = {Porcentagem * 100}%'.format(NovoS=NovoS,
                                                   Aumento=Aumento,
                                                   Porcentagem=Porcentagem))
elif Salario > 3000 and Salario < 8000 or Salario == 8000:
    Porcentagem = float(10/100)
    Aumento = Salario * Porcentagem
    NovoS = Salario + Aumento
    print(f'Novo salario = {NovoS:.2f}',
          f'\nAumento = {Aumento:.2f}',
          f'\nPorcentagem = {Porcentagem * 100}%'.format(NovoS=NovoS,
                                                   Aumento=Aumento,
                                                   Porcentagem=Porcentagem))
elif Salario > 8000:
    Porcentagem = float(5/100)
    Aumento = Salario * Porcentagem
    NovoS = Salario + Aumento
    print(f'Novo salario = {NovoS:.2f}',
          f'\nAumento = {Aumento:.2f}',
          f'\nPorcentagem = {Porcentagem * 100}%'.format(NovoS=NovoS,
                                                   Aumento=Aumento,
                                                   Porcentagem=Porcentagem))



