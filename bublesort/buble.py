# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Bublesort


def bubblesort(dados):
	for d in range(len(dados)):
		troca = False
		for i in range(0,len(dados) -1):
			if dados[i] > dados[i+1]:
				dados[i],dados[i+1] = dados[i+1], dados[i]
				troca = True
		if not troca:
			break

