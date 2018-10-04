# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Seleciona Divisores em uma Lista


def filtra_divisores(lista):
	for j in range(len(lista) -1 ,-1,-1):
		somatorio = 0
		d = str(lista[j])
		for i in d:
			somatorio += int(i)
		if  lista[j] % somatorio != 0:
			lista.pop(j)
