# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Pi

erro = float(raw_input())

pi = 1/1.0

pi_anterior = 4 * pi
print "%.6f" % pi_anterior

pos = 0
denominador = 3.0
while True:
	pos += 1
	if pos % 2 == 0:
		pi += 1 / denominador
	else:
		pi -= 1 / denominador
	denominador += 2.0
	novo_pi = 4 * pi
	print "%.6f" % novo_pi
	if abs(novo_pi -  pi_anterior) < erro:
		break
	pi_anterior = novo_pi
