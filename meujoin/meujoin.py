# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Meu Join


def meu_join(delimitador,lista):
	string = ''
	for i in range(len(lista)):
		if i +1 != len(lista):
			string += lista[i] + delimitador
		else:
			string += lista[i]
	return string
