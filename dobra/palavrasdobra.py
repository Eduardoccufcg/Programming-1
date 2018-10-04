# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Palavra dobradas

n = int(raw_input())
dobradas = []
nao_dobradas = []
for i in range(n):
	palavra = raw_input()
	tem_letras_dobradas = False
	for j in range(1,len(palavra)):
		letra = palavra[j]
		anterior = palavra[j-1]
		if letra == anterior:
			tem_letras_dobradas = True
			dobradas.append(palavra)
			break
		
	if tem_letras_dobradas == False:
		nao_dobradas.append(palavra)
	
print '%d palavra(s) com letras dobradas:' % len(dobradas)
for i in dobradas:
	print i
print'---'
print '%d palavra(s) sem letras dobradas:' % len(nao_dobradas)
for e in  nao_dobradas:
	print e	

