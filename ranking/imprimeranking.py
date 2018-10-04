# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Imprime ranking

n = int(raw_input())

ponto = 0
indice = 1

for i in range(1,n+1):
	time = raw_input()
	pontos =  int(raw_input())
	if pontos != ponto:
		indice = i
	ponto = pontos

	print '%d. %s (%d)' % (indice,time,ponto)
