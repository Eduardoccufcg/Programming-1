# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Filtrando Elementos em uma Lista


def filtra_lista(num, lista):
	lista_nova = []
	for i in range(len(lista)):
		if i % num == 0:
			lista_nova.append(lista[i])
	return lista_nova
