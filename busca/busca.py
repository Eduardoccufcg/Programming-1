# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Busca Linear



seq = [8, 9, 2, 3, 6, 10, 7, 9]

def busca(seq,valor):
	
	e = 0
	for i in range(len(seq)):
		if seq[i] == valor:
			return i
			break
		else:
			e += 1
	if e == len(seq):
		return -1	
