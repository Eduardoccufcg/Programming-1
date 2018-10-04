# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Quantidade e média de numeros pares

numeros_lidos = int(raw_input())

soma_pares = 0
contador_pares = 0
lista_de_numeros = []
for c in range(numeros_lidos):
	numeros = int(raw_input())
	lista_de_numeros.append(numeros)
	if numeros % 2 == 0:
		contador_pares += 1
		soma_pares += numeros

media = float(soma_pares) / contador_pares
abaixo = 0
for i in lista_de_numeros:
	if i < int(media):
		abaixo +=1
		
print'soma: %d' % soma_pares
print'média: %.1f' % media
print '%d número(s) abaixo da média' % abaixo

