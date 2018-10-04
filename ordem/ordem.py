# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Ordem alfabética

depois = 0
antes = 0

lista = []
n_palavras_ler = int(raw_input())

for i in range(n_palavras_ler):
	palavras_sequencia = raw_input()
	lista.append(palavras_sequencia)
print'---'
palavra_referencia = raw_input()
for i in range (len(lista)):
	if lista[i] == palavra_referencia:
		depois -= 1	
		depois += 1
	elif lista[i]> palavra_referencia:
		depois += 1
	else:
		antes += 1
print '%d antes' % antes
print '%d depois' % depois

	
