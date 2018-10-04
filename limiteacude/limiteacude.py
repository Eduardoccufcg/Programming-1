# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Limite açude

limite_superior = float(raw_input())
nivel_atual = float(raw_input())

nivel = nivel_atual

while True:
	if nivel >= limite_superior:
		break
	entrada = raw_input().split()
	if entrada[0] == 'afluente':
		nivel += float(entrada[1])
	if entrada[0] == 'chuva':
		nivel += float(entrada[1])
	if entrada[0] == 'demanda':
		if nivel >= float(entrada[1]):
			nivel += float(entrada[1]) * (-1)
		

if nivel >= limite_superior:
	print'Açude passou a liberar água.'
print'Nível: %.2f' % nivel
