# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: série impares

for i in range(1,102,2):
	if i % 3 == 0 or i % 5 == 0:
		 i = '*'
	
	print i
