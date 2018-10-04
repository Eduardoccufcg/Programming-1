# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Imprime Sequencias

numero_alvo = int(raw_input())
contador = 0
i = 0
while True:
	entrada = raw_input()
	i += 1
	contador = 0	
	if entrada == 'fim':
		break
	entrada2 = entrada.split()
	for d in entrada2:
		if int(d) > numero_alvo:
			contador += 1
	if contador > len(entrada2) / 2:
		print 'sequencia %d: %s' % (i,entrada)


