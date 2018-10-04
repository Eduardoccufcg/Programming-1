# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Conjunto com mais elementos


elementos = 0
lista_q_elementos = []
while True:
	numeros = raw_input()
	if numeros == 'fim':
		break
	if int(numeros) >= 0:
		elementos += 1
	else:
		lista_q_elementos.append(elementos)
		elementos = 0
contador = 0
maior = 0
if lista_q_elementos != []:
	for i in range(len(lista_q_elementos)):
		if int(lista_q_elementos[i]) > maior:
			maior = int(lista_q_elementos[i])
			
	for d in range(len(lista_q_elementos)):
		if lista_q_elementos[d] == maior:
			break
		else:
			contador += 1
		
	print'Conjunto %d - %d elemento(s)' % (contador+1,maior)
