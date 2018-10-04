# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Maior Palavra de Uma frase


def maior_palavra(frase):
	
	palavra_maior = ''
	palavra = ''

	for i in frase:
		if i != ' ':
			palavra += i
		else:
			if len(palavra_maior) <= len(palavra):
				palavra_maior = palavra
			palavra = ''
	if len(palavra_maior) <= len(palavra):
				palavra_maior = palavra
	return palavra_maior
