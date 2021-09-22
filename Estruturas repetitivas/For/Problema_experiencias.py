# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para
# organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
# quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este
# laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas
# informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
# utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um
# valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um
# inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo
# de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de
# cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o
# percentual deve ser apresentado com dois dígitos após o ponto.

x = int(input('Quantos casos de teste serao digitados?'))

total = 0
totalq = 0
totalr = 0
totals = 0


for i in range(0,x):
    q = int(input('Quantidade de cobaias:'))
    t = str(input('Tipo de cobaia:'))
    total = total + q
    if t == "C":
        totalq = totalq + q
    elif t == "R":
        totalr = totalr + q
    elif t == "S":
        totals = totals + q

mediac = (totalq / total) * 100
mediar = (totalr / total) * 100
medias = (totals / total) * 100



print('\nRELATORIO FINAL:'
      f'\nTotal: {total} cobaias'
      f'\nTotal de coelhos: {totalq}'
      f'\nTotal de rato: {totalr}'
      f'\nTotal de sapos: {totals}'
      f'\nPercentual de coelhos: {mediac:.2f}'
      f'\nPercentual de ratos: {mediar:.2f}'
      f'\nPercentual de sapos: {medias:.2f}')


