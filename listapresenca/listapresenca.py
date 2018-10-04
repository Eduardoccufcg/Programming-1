# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Lista Presença

def cria_lista_presenca(turmas,nomes,num):
	lista = []
	for i in range(len(turmas)):
		if turmas[i] == num:
			lista.append(nomes[i])

	return lista
