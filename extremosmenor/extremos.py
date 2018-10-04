# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: extremos

n_lidos = int(raw_input())

lista_numeros = []
for c in range(n_lidos):
	numeros = int(raw_input())
	lista_numeros.append(numeros)
lista_extremos = []
extremo1 = 0
for v in lista_numeros:
	extremo1 += v
	lista_extremos.append(extremo1)
	break
extremo2 = 0
for u in range(len(lista_numeros)-1,-1,-1):
	extremo2 += lista_numeros[u]
	lista_extremos.append(extremo2)
	break
menor = lista_extremos[0]
for i in lista_extremos:
	if i < menor:
		menor = i
abaixo = 0
acima = 0
for c in lista_numeros:
	if c < menor:
		abaixo += 1
	elif c > menor:
		acima += 1
print 'Menor dos extremos: %d' % menor
print '%d número(s) abaixo do menor' % abaixo
print '%d número(s) acima do menor' % acima
		




