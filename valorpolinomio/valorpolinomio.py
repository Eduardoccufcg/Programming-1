# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Valor Polinômio


def valor_polinomio(polinomio, valor):	
	soma = 0
	for i in range(len(polinomio)-1,-1,-1):
		resultado = polinomio[i] * valor ** i
		soma += resultado
	return soma
