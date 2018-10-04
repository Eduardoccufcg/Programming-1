# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Depois do 13 Nada

n1 = int(raw_input())
n2 = int(raw_input())
n3 = int(raw_input())

if n1 != 13 and n2 != 13 and n3 != 13:
	soma = n1 + n2 + n3
	if soma == 13:
		soma = 0
elif n1 == 13 and n2 != 13 and n3 != 13 or n3 == 13:
	soma = 0
elif n1 != 13 and n2 == 13 and n3 != 13 or n3 == 13:
	soma = n1
	if soma ==13:
		soma = 0
if n1 != 13 and n2 != 13 and n3 == 13:
	soma =  n1 + n2
	if soma == 13:
		soma = 0

print soma
