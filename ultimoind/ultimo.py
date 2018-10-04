# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Último Índice

def ultimo_indice(num,lista):
	ta_na_lista = False
	for i in range(len(lista)-1,-1,-1):
		if lista[i] == num:
			indice = i
			ta_na_lista = True
			break
	if ta_na_lista == False:
		d = -1		
	else:
		d = indice
	return d
