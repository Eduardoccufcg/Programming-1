# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Guerra Baralho

jogador1 = 0
jogador2 = 0
empate = 0
while True:
	entrada = raw_input().split()
	if entrada == ['0','0']:
		break
	if int(entrada[0]) > int(entrada[1]):
		jogador1 += 1
	elif int(entrada[0]) < int(entrada[1]):
		jogador2 += 1
	else:
		empate += 1

print 'Jogador 1: %d, Jogador 2: %d, Empates: %d' % (jogador1, jogador2, empate)
