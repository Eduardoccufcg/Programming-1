# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Conjunto Maiores

lista_indice = []
lista_soma = []
limite = int(raw_input())
n_conjuntos = int(raw_input())
indice = 0
soma = 0
while n_conjuntos != 0:
	numero = int(raw_input())
	if numero < 0:
		lista_soma.append(soma)
		indice += 1
		lista_indice.append(indice)
		n_conjuntos -= 1
		soma = 0
	else:
		soma += numero
for i in range(len(lista_soma)):
	if lista_soma[i] > limite:
		print'conjunto %d: %d' % (lista_indice[i],lista_soma[i])	
	
