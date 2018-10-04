# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Vogais Primeiro

def vogais_primeiro(palavra):
	palavranova = ''
	palavranova2 = ''
	for i in palavra:
		if i in 'AEIOUaeiou':
			palavranova += i
		else:	
			palavranova2 += i
	return palavranova + palavranova2
	
