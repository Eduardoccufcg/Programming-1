# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: PlifPlof
# Programação 1 / 2017.2

numero_1 = int(raw_input())
numero_2 = int(raw_input())
numero_3 = int(raw_input())
soma = numero_1 + numero_2 + numero_3

if soma % 3 == 0  and soma % 5 == 0:
	print 'plifplof'
elif soma % 5 == 0:
	print 'plof'
elif soma % 3 == 0:
	print 'plif'
else:
	print soma
