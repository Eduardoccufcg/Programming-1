# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Quantidades de Inteiros diviseis por k

numero_k = int(raw_input())
numero_n = int(raw_input())
lista_inteiros = []
e_divisivel = 0
for i in range(numero_n):
	numeros = raw_input()
	lista_inteiros.append(numeros)
	
for i in lista_inteiros:
	
	if int(i) % numero_k == 0:
		e_divisivel += 1
print'%d (%.1f%%)' % (e_divisivel,(e_divisivel * 100.0) / len(lista_inteiros))
	
