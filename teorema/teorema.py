# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Teorema de Herao

import math

n = int(raw_input())
soma = 0
maiores = 0
area_de_comparacao = 100.00

listaarea = []
for i in range(n):
	lados = raw_input().split()
	a,b,c = float(lados[0]),float(lados[1]),float(lados[2])
	s = (a + b + c) / 2
	area = math.sqrt((s * (s-a)) * (s-b) * (s-c))
	listaarea.append(area)
	if area > area_de_comparacao:
		maiores += 1
		soma += area
for d in range(len(listaarea)):
	
	print 'Área %s: %.2f' % (d+1,listaarea[d])
	
if maiores != 0:
	print'Número maiores: %d, área média: %.2f' % (maiores , soma / maiores)


	

