# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Tabela de quadrados

x = int(raw_input())
y = int(raw_input())

if x > y:
	print "---"
else:
	for i in range(x,y + 1):
		print i, i ** 2
	
