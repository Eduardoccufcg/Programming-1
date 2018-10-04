# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Remove Números Opostos Adjacentes


def anula(lista):
	i = 0
	while i < len(lista) -1:
		if lista[i+1] + lista[i] == 0:
			lista.pop(i+1)
			lista.pop(i)
			i -= 2
		i += 1
