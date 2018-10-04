# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Karel, o robô

x = 0
y = 0

while True:
	coordenada = raw_input().split()
	if coordenada[1] == '0':
		print'Fim de jogo'
		break
	if coordenada[0] == 'B':
		y += int(coordenada[1]) * (-1)
	if coordenada[0] == 'E':
		x += int(coordenada[1]) * (-1)
	if coordenada[0] == 'C':
		y += int(coordenada[1])
	if coordenada[0] == 'D':
		x += int(coordenada[1])
	if abs(y) == 2 * abs(x) and x!=0 and y!=0:
		print'Parabéns, conquista do portal (%d, %d)' % (x,y)
		break

