# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Porta Eletronica
pesquisa = 0

lista = []
while True:
	entrada = raw_input().split()
	if entrada[0] == 'S':
		break
	if entrada[0] == 'R':
		lista.append(entrada[1])
	elif entrada[0] == 'P':
		for d in range(len(lista)):
			if lista[d][0] == entrada[1]:
				pesquisa += 1
		print pesquisa
		pesquisa = 0

