# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Maioridade Penal Função

def maioridade_penal(string1,string2):
	string1 = string1.split()
	string2 = string2.split()
	string_nova = ''
	for d in range(len(string2)):
		if int(string2[d]) >= 18:
			if d+1 < len(string2):
				string_nova += string1[d] + ' '
			else:
				string_nova += string1[d]
		
	return string_nova

