# Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
# formato horas:minutos:segundos.

# Inserir Valores

Segundos = int(input('Digite a duracao em segundos:'))

# Cálculo Valores

Horas = Segundos // 3600 # Divisão Inteira
Resto = Segundos % 3600  # Pega Resto da Divisão Inteira

Minutos = Resto // 60 # Pega Resto do Resto e transofrma em minutos fazendo uma divisão Inteira
SegundosR = Resto % 60 # E por fim resto da divisão minutos em segundos.

# Imprimir Valores

print(Horas, ':', Minutos, ':', SegundosR)