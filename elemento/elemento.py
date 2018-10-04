# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: encontrar elemento

numero = int(raw_input())

sequencia = raw_input().split()
contador = 0
for i in range(len(sequencia)):
	if sequencia[i] == str(numero):
		contador =+ 1
if contador != 0:		
	print 'sim'
else:
	print 'não'
