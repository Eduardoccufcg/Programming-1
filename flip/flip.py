# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Flip


def flip(lista,i,j):
	for i in range(i,j+1):
		lista[i] , lista[j] = lista[j], lista[i]
		i += 1
		j -= 1
		if j - i < 1:
			break
