# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Espaço por virgula


frase_final = ''

frase = raw_input()
i = int(raw_input())
j = int(raw_input())

for d in range(i, j):
	if d != (j - 1):
		if frase[d] != ' ':
			frase_final += '%s '%frase[d]
		elif frase[d] == ' ':
			frase_final+= ', '
	elif d == (j - 1):
		if frase[d] != ' ':
			frase_final += '%s'%frase[d]
		elif frase[d] == ' ': 
			frase_final += ','	
	
print frase_final
	
