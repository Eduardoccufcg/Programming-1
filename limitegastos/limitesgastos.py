# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Limites de gastos
lista = []
limite = float(raw_input())
soma = 0
aux = ''
while True:
	entrada = raw_input()
	if entrada == 'fim':
		break
	entrada2 = entrada.split()
	for i in range(len(entrada2) -1):
		aux += '%.1f ' % float(entrada2[i])
	aux += '%.1f' % float(entrada2[-1])
	for i in entrada2:
		soma += float(i)
	media = soma / len(entrada2)
	if media * 2 <= limite:
		break
	soma = 0
	if media > limite:
		lista.append(aux)
	aux = ''
		
for i in lista:
	print i
