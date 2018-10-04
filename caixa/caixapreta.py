# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Caixa preta

n_medicoes = int(raw_input())
validos = 0
for i in range(n_medicoes):
	
	dados = raw_input().split()
	achei_negativo = False
	peso, combustivel, altitude = int(dados[0]),int(dados[1]),int(dados[2])
	if peso < 0 or combustivel < 0 or altitude < 0:
		achei_negativo = True
			
	if peso >= 0:
		validos += 1
	else:
		achei_negativo = True
		print 'dado inconsistente. peso negativo.'
		
		break
	if combustivel >= 0:
		validos += 1
	else:
		achei_negativo = True
		print 'dado inconsistente. combustível negativo.'
		
		break
	if altitude >= 0:
		validos += 1
	else:
		achei_negativo = True
		print 'dado inconsistente. altitude negativa.'
		
		break
print '%i dados válidos.' % validos
