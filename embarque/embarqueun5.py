# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Embarque organizado

pares = ''
impares = ''
string = ''
embarque = raw_input().split()
embarquestr = ''

for i in embarque:
	embarquestr += i
	if int(i) % 2 == 0:
		pares += i
	else:
		impares += i
		
string = impares + pares
if embarquestr == string:
	print'ok'
else:
	print'erro'
