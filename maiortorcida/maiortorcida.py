# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Maior Torcida

lista_torcedores = []
for t in range(10):
	q_torcedores = raw_input()
	lista_torcedores.append(q_torcedores)
soma_2time = 0
soma_total = 0
for i in range(5,len(lista_torcedores)):
	soma_2time += int(lista_torcedores[i])
for i in range(len(lista_torcedores)):
	soma_total += int(lista_torcedores[i])
	
soma_1time = soma_total - soma_2time

if soma_1time > soma_2time:
	print'O primeiro time leva mais torcedores ao estádio.'
elif soma_2time > soma_1time:
	print'O segundo time leva mais torcedores ao estádio.'
else:
	print'Empate.'
	
