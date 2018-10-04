# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Limpeza

def meu_replace(a,b):
	nova = ''
	lista = []
	total_string = ''
	for i in total2:
		if i != a:
			nova += i
		else:
			lista.append(nova)
			nova = ''
	lista += nova
	for i in range(len(lista)):
		if  i != len(lista) -1:
			total_string += lista[i] + b
		else:
			total_string += lista[i] + '0'
	return total_string 	


servico = int(raw_input())
# fossa
if servico == 1:
	metro = int(raw_input())
	total = metro * 80.00
	total2 = str(total)
	
	print'R$ %s' % meu_replace('.',',')
	if total >= 200.00:
		print'Brinde!'
# caixa d'agua
elif servico == 2:
	metro = int(raw_input())
	total = metro * 50.00
	total2 = str(total)
	
	print'R$ %s' % meu_replace('.',',')
	if total >= 200.00:
		print'Brinde!'
# caixa_de_esgoto
elif servico == 3:
	print'R$ 50,00'
	
