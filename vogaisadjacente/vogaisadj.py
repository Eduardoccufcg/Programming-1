# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Tem Vogais Adjacentes

def tem_vogais_adjacentes(palavra):
	vogais = 'aeiouAEIOU'
	tem_vogais_adjacentes = False
	for d in range(len(palavra) -1 ):
		if palavra[d] in vogais and palavra[d+1] in vogais:
			tem_vogais_adjacentes = True
	if tem_vogais_adjacentes == True:
		return'sim'
	else:
		return'nao'
palavra = raw_input()
print tem_vogais_adjacentes(palavra)
