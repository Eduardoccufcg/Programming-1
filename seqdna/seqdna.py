# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: sequencia de DNA

seq1 = raw_input()
seq2 = raw_input()
contador_iguais = 0
for i in range(len(seq1)):
	if seq1[i] == seq2[i]:
		contador_iguais += 1
if contador_iguais <= len(seq1) / 2:
	print 'nao'
else:
	print'sim'
