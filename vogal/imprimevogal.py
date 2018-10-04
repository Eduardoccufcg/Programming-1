# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Imprime Primeira vogal

vogais = 'aeiouAEIOU'
palavra = raw_input()


listapalavra = []
for i in palavra:
	if i in vogais:
		listapalavra.append(i)
if listapalavra != []:
	print listapalavra[0]
else:
	print "-"
