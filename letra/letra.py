# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Classifica letra

string = 'aeiouAEIOU'
palavra = raw_input()

for i in range(len(palavra)):
	if palavra[i] in string:
		print'<%s> sim' % palavra[i]
	else:
		print'<%s> nao' % palavra[i]
