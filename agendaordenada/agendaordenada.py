# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Agenda Ordenada


def agenda_ordena(dados,nome):
	lista_agenda = []
	for d in range(len(dados)):
		troca = False
		for i in range(0,len(dados) -1):
			if dados[i] > dados[i+1]:
				dados[i],dados[i+1] = dados[i+1], dados[i]
				troca = True
		if not troca:
			break
	for i in dados:
		if i == nome:
			lista_agenda.append('* %s' % nome)
		else:
			lista_agenda.append(i)
	return lista_agenda

lista = []
while True:
	nome = raw_input()
	if nome == '####':
		break
	lista.append(nome)
	for d in agenda_ordena(lista,nome):
		print d
	print'----'
