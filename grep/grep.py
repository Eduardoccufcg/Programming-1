# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Grep
i = 0
palavra = raw_input()
n = int(raw_input())

for u in range(n):
	frase = raw_input()
	for d in frase:
		if  d == palavra[i]:
			i +=1
			if i == len(palavra):
				print frase
				i = 0
		else:
			i = 0

