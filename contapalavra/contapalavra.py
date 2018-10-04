# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Conta Palavras

def conta_palavras(k,palavras):
	cont = 0
	palavra = palavras.split(':')
	for i in palavra:
		if len(i) >= k:
			cont += 1	
	return cont

