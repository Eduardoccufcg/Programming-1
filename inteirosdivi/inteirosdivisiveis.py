# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: inteiros divisiveis

a = int(raw_input())
b = int(raw_input())
k = int(raw_input())

for i in range(1,k+1):
	if i % a == 0 and i % b == 0:
		print i
