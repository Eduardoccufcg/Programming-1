# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Caixa preta

pesos_validos = 0
combustiveis_validos = 0
altitude_validas = 0
validos = 0

achei_negativo = False

while achei_negativo == False:
	dados = raw_input().split()
	peso, combustivel, altitude = int(dados[0]),int(dados[1]),int(dados[2])
	if peso < 0 or combustivel < 0 or altitude < 0:
		achei_negativo = True
		
	if peso >= 0:
		pesos_validos +=1
	else:
		print 'dado inconsistente. peso negativo.'
		achei_negativo = True
		break
	if combustivel >= 0:
		combustiveis_validos += 1
	else:
		print 'dado inconsistente. combustível negativo.'
		achei_negativo = True
		break
	if altitude >= 0:
			altitude_validas += 1
	else:
		print 'dado inconsistente. altitude negativa.'
		achei_negativo = True
		break
		

		
print'peso: %d' % pesos_validos
print'combustível: %d' % combustiveis_validos
print'altitude: %d' % altitude_validas

