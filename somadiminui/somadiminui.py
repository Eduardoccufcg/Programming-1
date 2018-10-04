# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Soma e diminui vizinhos


def soma_diminui_vizinhos(lista):
	resultado = 0
	for i in range(len(lista)):
		if i == 0:
			resultado += lista[i]
		elif i % 2 == 0:
			resultado -= lista[i]
		else:
			resultado += lista[i]
	
	return resultado
		
		
