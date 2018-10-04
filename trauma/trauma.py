# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Hospital de Trauma

def cadastra(fila, nome, prioridade):
	j = 0
	for d in range(len(prioridade)):
		troca = False
		for i in range(0,len(fila)):
			if fila[i] == prioridade[d]:
				nome[i],nome[j] = nome[j], nome[i]
				j += 1
				troca = True
		if not troca:
			break
	return nome

def resumo(fila):
	cont_vermelho = 0
	cont_laranja = 0
	cont_amarelo = 0
	cont_verde = 0
	cont_azul = 0
	for i in range(len(fila)):
		if fila[i] == 'vermelho':
			cont_vermelho += 1
		elif fila[i] == 'laranja':
			cont_laranja += 1
		elif fila[i] == 'amarelo':
			cont_amarelo += 1
		elif fila[i] == 'verde':
			cont_verde += 1
		elif fila[i] == 'azul':
			cont_azul += 1
	lista = [cont_vermelho, cont_laranja,cont_amarelo,cont_verde,cont_azul]
	return lista		


			
fila = []
nome = []
prioridade = ['vermelho', 'laranja', 'amarelo', 'verde', 'azul']

while True:
	pacientes = raw_input().split()
	if pacientes == ['fim']:
		break
	fila.append(pacientes[1])
	nome.append(pacientes[0])
for i in cadastra(fila,nome,prioridade):
	print i
print'---'
for i in range(len(resumo(fila))):
	print '%s: %d' % (prioridade[i],resumo(fila)[i])
print'---'

