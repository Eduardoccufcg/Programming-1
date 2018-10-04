# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: lucro mensal
lista_lucro = []

meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']

for d in range(12):
	valores = raw_input().split()
	receita, despesa = float(valores[0]), float(valores[1])
	lucro = receita - despesa
	lista_lucro.append(lucro)
		
for i in range(len(meses)):
	if lista_lucro[i] < 0:
		print meses[i],lista_lucro[i]
	else:
		print meses[i],'',lista_lucro[i]
	
