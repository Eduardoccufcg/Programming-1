# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Mais consoantes

vogais = 0
consoantes = 0
palavras_lidas = 0
while True:
	palavra = raw_input()
	palavras_lidas += 1
	for i in palavra:
		if i in 'AEIOUaeiou':
			vogais += 1
		else:
			consoantes += 1
	if consoantes > vogais:
		break
	vogais = 0
	consoantes = 0
	
print palavras_lidas

