# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: média_atinge_limite

lista = []
while True:
	sequencia = raw_input()
	if sequencia == '-':
		break
	lista.append(sequencia)
	
limite_media = float(raw_input())
media = 0
n_termos = 0
soma = 0
for i in range(len(lista)):
	if media < limite_media:
	cd	n_termos += 1
		soma += float(lista[i])
		media = soma / n_termos	

if media <= limite_media:

	print'limite não alcançado'
else:
	print'media = %.1f' % media
	print'num = %d' % n_termos

