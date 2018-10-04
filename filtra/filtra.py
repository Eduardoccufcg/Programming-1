# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Filtrando Elementos e Alterando uma Lista


def filtra_altera_lista(num, lista):
	for i in range((len(lista) -1),-1,-1):
		if i % num != 0:
			lista.pop(i)
			

