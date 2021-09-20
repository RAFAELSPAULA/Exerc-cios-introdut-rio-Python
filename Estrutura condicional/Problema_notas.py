# Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de
# uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no
# ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a
# mensagem "REPROVADO".

#Inserindo Valores

PrimeiraN = float(input('Digite a primeira nota: '))
SegundaN = float(input('Digite a primeira nota: '))

# Calculando Valores

soma = (PrimeiraN + SegundaN)

# Estabelecendo condição para ver se foi aprovado ou não

Resultado = (f'Nota FINAL: {soma:.1f}'.format(soma=soma))

if soma > 60 or soma == 60:
    input(Resultado)
else:
    input('REPROVADO')

