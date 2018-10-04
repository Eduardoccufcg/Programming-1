# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Soma os Divisores do Primeiro Elemento de uma Lista

lista = []
for i in range(11):
	numero = int(raw_input())
	lista.append(numero)
numero_comparador = lista[0]
lista = lista[1:]

for i in lista:
	if numero_comparador % i == 0:
		print i
	
