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
		lista_q_elementos.append(int(elementos))
		elementos = 0
maior = lista_q_elementos[0]
j = 0
for i in lista_q_elementos:
	j += 1
	if i >= maior:
		maior = i
print'Conjunto %d = %d elementos(s)' % (j,maior)
