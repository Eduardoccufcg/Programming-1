# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Inserção ordenada do primeiro elemento de uma lista

def insere_ordenado_primeiro(lista):
	for d in range(len(lista)):	
		for i in range(len(lista)-1):
			if lista[i] > lista[i+1]:
				lista[i], lista[i+1] = lista[i+1], lista[i]		
		
