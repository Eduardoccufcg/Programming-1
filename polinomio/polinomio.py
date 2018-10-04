# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Aplicação Polinômios


lista = []
def polinomio(entrada2 , x):
	soma = 0
	for i in range(len(entrada2)-1,0,-1):
		resultado =  int(entrada2[i]) * x ** (i -1)
		soma += resultado
	return soma
	
while True:
	entrada = raw_input()
	if entrada == 'fim':
		break
	if entrada[0] == 'p':
		lista.append('novo polinomio')
		entrada2 = entrada.split()
	else:
		x = int(entrada)
		lista.append(polinomio(entrada2 , x))
		
for i in lista:
	print i
