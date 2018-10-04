# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Um Passo do Algoritmo BubbleSort
lista2 = []
def bubblesort_step(dados):
	
	for d in range(len(dados)):
		troca = False
		for i in range(0,len(dados) -1):
			if dados[i] > dados[i+1]:
				dados[i],dados[i+1] = dados[i+1], dados[i]
				troca = True
		if not troca:
			break
		break
	lista_sem_split = ''
	for i in range(len(dados)):
		if i != len(dados) -1:
			lista_sem_split += str(dados[i]) + ' '
		else:
			lista_sem_split += str(dados[i])
	return lista_sem_split

lista_final = []
while True:
	lista = raw_input().split()
	if lista == ['fim']:
		break
	for i in lista:
		lista2.append(int(i))
	lista_final.append(bubblesort_step(lista2))
	lista2 = []
	
for i in lista_final:
	print i	
