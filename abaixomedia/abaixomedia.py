# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Abaixo da média
n_numeros = 0
soma = 0
lista_numeros = []
while True:
	numeros = raw_input()
	if numeros == 'fim':
		break
		
	else:
		lista_numeros.append(numeros)
		n_numeros += 1
		soma += float(numeros)
		
	media = soma / n_numeros
	
print'%.2f' % media

for i in range(len(lista_numeros)):
	if float(lista_numeros[i]) < media:
		print i+1 , lista_numeros[i]
