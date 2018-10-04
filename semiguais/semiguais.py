# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Remove Palavras com Letras Iguais Consecutivas


def remove_consecutivas(lista):
	for i in range(len(lista) -1 ,-1,-1):
		tem_consecutivas = False
		for d in range(len(lista[i]) - 1):
			if lista[i][d] == lista[i][d+1] or lista[i][d] == lista[i][d+1].lower() or lista[i][d] == lista[i][d+1].upper() :
				tem_consecutivas = True
		if tem_consecutivas == True:
			lista.pop(i)
