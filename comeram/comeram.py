# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Quantos Comeram

def quantos_comeram(N,fila):
	i = 0
	vendas = 0
	while True:
		if fila[i] < N:
			vendas += fila[i]
			N -= fila[i]
		elif fila[i] == N:
			vendas += N
			N -= fila[i]
			break
		elif fila[i] > N:
			break
		i += 1
	return vendas
