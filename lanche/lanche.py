# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Lanche mais pedido


def lanchemaispedido(dados):
	for i in range(len(dados)):
		d = i
		j = 0
		if dados[i] == dados[d]:
			dados[i],dados[j] = dados[j], dados[i]
			j += 1
	cont = 0	
	for i in dados:
		if i == dados[0]:
			cont += 1

	if cont > len(dados) / 2:
		return dados[0]
