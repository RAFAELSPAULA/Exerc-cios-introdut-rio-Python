# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo
# pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

# Inserindo Valores

HoraI = float(input('Hora inicial: '))
HoraF = float(input('Hora final: '))

# Condição para executar

if HoraF < HoraI or HoraF == HoraI:
    HoraF = HoraF + 24.00
    Duracao = HoraF - HoraI
    print(f'O JOGO DUROU {Duracao:.0f} HORA(S) ')
