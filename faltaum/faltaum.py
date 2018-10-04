# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Falta um

def encontra_rotulo_perdido(l1,l2):
	for i in range(len(l2)):
		for d in range(len(l1)-1,-1,-1):
			if l1[d] == l2[i]:
				l1.pop(d)
	for i in l1:
		return i
