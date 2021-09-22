# Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa.
# Para isto, mandou digitar um conjunto de N mercadorias, cada uma contendo nome, preço de compra e preço de
# venda das mesmas. Fazer um programa que leia tais dados e determine e escreva quantas mercadorias proporcionaram:
#  lucro < 10%
#  10% ≤ lucro ≤ 20%
#  lucro > 20%
# Determine e escreva também o valor total de compra e de venda de todas as mercadorias, assim como o lucro total.

n = int(input("Serao digitados dados de quantos produtos? "))

nomes: [str] = [0 for x in range(n)]
pcompra: [float] = [0 for x in range(n)]
pvenda: [float] = [0 for x in range(n)]
porcentagemlucros: [float] = [0 for x in range(n)]

for i in range(0,n):
	print(f"Produto {i + 1}:")
	nomes[i] = str(input("Nome: "))
	pcompra[i] = float(input("Preco de compra: "))
	pvenda[i] = float(input("Preco de venda: "))

for i in range(0,n):
	porcentagemlucros[i] = (pvenda[i] - pcompra[i]) / pcompra[i] * 100.0

abaixo = 0
entre = 0
acima = 0

for i in range(0,n):
	if porcentagemlucros[i] < 10.0:
		abaixo = abaixo + 1
	elif porcentagemlucros[i] < 20.0:
		entre = entre + 1
	else:
		acima = acima + 1

vtotalcompra = 0
vtotalvenda = 0

for i in range(0,n):
	vtotalcompra = vtotalcompra + pcompra[i]
	vtotalvenda = vtotalvenda + pvenda[i]

lucrototal = vtotalvenda - vtotalcompra

print("\nRELATORIO:")
print(f"Lucro abaixo de 10%: {abaixo}")
print(f"Lucro entre 10% e 20%: {entre}")
print(f"Lucro acima de 20%: {acima}")
print(f"Valor total de compra: {vtotalcompra:.2f}")
print(f"Valor total de venda: {vtotalvenda:.2f}")
print(f"Lucro total: {lucrototal:.2f}")