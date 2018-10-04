# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Questões para P1
soma_total = 0
contador = 0
lista_nomes = []
lista_soma = []
soma = 0
while True:
	entrada = raw_input()
	contador += 1
	if entrada == '**':
		break
	if entrada == '*':
		lista_soma.append(soma)
		soma = 0
		contador = 0
	if contador == 1:
		lista_nomes.append(entrada)
	elif contador > 1:
		soma_total += int(entrada)
		soma += int(entrada)
print'Relatório de novas questões:'
print			
for i in range(len(lista_nomes)):
	print'%s: %d' % (lista_nomes[i],lista_soma[i])	
print'---'
print'Total de novas questões: %d' % soma_total
