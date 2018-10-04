# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Tiro ao alvo
lista = []
soma = 0
import math
y1 = 0.0
x1 = 0.0

while True:
	x2 = float(raw_input())
	y2 = float(raw_input())
	distancia = math.sqrt((x2 - x1) ** 2 + (y2 -y1) ** 2)
	if distancia <= 200.0:
		soma += distancia
		lista.append(distancia)
	if distancia > 200.0:
		break
	x2 = x1
	y2 = y1

melhor_tiro = lista[0]

for i in lista:
	if i <= melhor_tiro:
		melhor_tiro = i
		print'%.2f cm (melhor tiro)' % i
	else:
		print'%.2f cm' % i
print'--'
print'num tiros: %d' % len(lista)
print'melhor tiro: %.2f cm' % melhor_tiro
print 'distancia media: %.2f cm' % (soma / len(lista))
	

