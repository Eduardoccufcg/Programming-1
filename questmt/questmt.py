# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: questões para mt

def seleciona_questoes(todas,utilizadas):
	for d in range(len(utilizadas)):
		for e in range(len(todas)-1,-1,-1):
			if utilizadas[d] == todas[e]:
				todas.pop(e)

todas = [1, 2, 3, 4, 5]
utilizadas = [3, 4]
seleciona_questoes(todas, utilizadas)
assert todas == [1, 2, 5]
