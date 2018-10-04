# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Promoção cliente
compras_joao = 0
compras_julio = 0
q_joao = 0
q_julio = 0
nome = ''
while True:
	clientecompra = raw_input().split()
	if clientecompra[0] == 'fim':
		break
	
	if clientecompra[0] == 'joao':
		compras_joao += float(clientecompra[1])
		q_joao += 1
	else:
		compras_julio += float(clientecompra[1])
		q_julio += 1
		
	if compras_joao >= 2000 or compras_julio >= 2000:
		break
	
	if q_joao > 2 or q_julio > 2:
		break
		
if q_joao > 2:
	print'joao foi o vencedor. Comprou mais de duas vezes no período.'
elif compras_joao >= 2000:
	print'joao foi o vencedor. Comprou mais R$ 2000.00 no período.'
elif q_julio > 2:
	print'julio foi o vencedor. Comprou mais de duas vezes no período.'
elif compras_julio >= 2000:
	print'julio foi o vencedor. Comprou mais R$ 2000.00 no período.'
else:
	print'Não houve vencedor.'
