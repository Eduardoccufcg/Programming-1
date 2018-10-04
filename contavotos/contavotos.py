# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Analytics assembreia


def conta_votos(votacao,id_votacao):
	sim = 0
	nao = 0
	for d in range(len(votacao)):
		if int(votacao[d].split(',')[2]) == id_votacao:
			if votacao[d].split(',')[1] == 'sim':
				sim += 1
			else:
				nao += 1
		
	return [sim, nao]

