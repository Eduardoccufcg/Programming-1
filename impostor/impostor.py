# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Insere Ordenado Impostor


def insere_ordenado_impostor(lista):
	e = 0
	while True:
		for i in range(len(lista)-1):
			if lista[i] > lista[i+1]:
				lista[i], lista[i+1] = lista[i+1], lista[i]		
		for d in range(len(lista)-1):
			if lista[d] < lista[d+1]:
				e += 1
		if e == len(lista) -1:
			break
		e = 0
	
