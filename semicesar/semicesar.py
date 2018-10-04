# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Semi César

def cesar(msg , d):
	palavra = ''
	alfabeto = 'abcdefghijklmnopqrstuvwxyz'
	for elemento in msg:
		teste = 0
		for i in range(len(alfabeto)):
			if elemento == alfabeto[i]:
				teste += 1
				if i + d < len(alfabeto) - 1:
					palavra += alfabeto[i+d]
				else:
					palavra += alfabeto[i + d - len(alfabeto)]
		if teste == 0:
			palavra += elemento
	return palavra
