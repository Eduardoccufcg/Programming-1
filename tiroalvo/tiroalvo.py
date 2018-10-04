# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Tiro ao alvo

soma = 0
import math
y1 = 0.0
x1 = 0.0
lista = []
while True:
	entrada = raw_input().split(',')

	x2 = float(entrada[0])
	y2 = float(entrada[1])
	distancia = math.sqrt((x2 - x1) ** 2 + (y2 -y1) ** 2)
	if distancia <= 200.0:
		soma += distancia
		lista.append(distancia)
		print'%.2f' % distancia
	if distancia > 200.0:
		break
	x2 = x1
	y2 = y1

	
print'--'
print'num disparos: %d' % len(lista)
print 'distancia media: %.2f' % (soma / len(lista) )
	

