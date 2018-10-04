# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Classificação de elementos utilizando a média dos extremos

n = int(raw_input())



lista = []
for i in range(n):
	num = int(raw_input())
	lista.append(num)
	maior = lista[0]
	menor = lista[0]
for i in lista:
	if i > maior:
		maior = i
for i in lista:
	if i < menor:
		menor = i
acima = 0
abaixo = 0		
media_extremos = (maior + menor) / 2.0
		
for i in lista:
	if float(i) < media_extremos:
		abaixo += 1
for i in lista:		
	if float(i) > media_extremos:
		acima += 1
			
print'Menor número: %d' % menor
print'Maior número: %d' % maior
print'Média dos extremos: %.2f' % media_extremos
print'%d número(s) abaixo da média' % abaixo
print'%d número(s) acima da média' %  acima	
