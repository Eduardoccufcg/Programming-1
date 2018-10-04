# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Calculadora



def soma(a,b):
	soma = a + b
	return soma
def subtracao(a,b):
	sub = a - b
	return sub
def multiplicacao(a,b):
	multi = a * b
	return multi
def divisao(a,b):
	divi = a / b 
	return divi
		
while True:
	entrada = raw_input().split()
	if entrada[0] == '5':
		break
	if entrada[0] == '4':
		a = int(entrada[1])
		b = int(entrada[2])
		if b != 0:
			print divisao(a,b)
		else:
			print'Erro: Divisão por 0'
			break
	if entrada[0] == '3':
		a = int(entrada[1])
		b = int(entrada[2])
		print multiplicacao(a,b)
	if entrada[0] == '2':
		a = int(entrada[1])
		b = int(entrada[2])
		print subtracao(a,b)
	if entrada[0] == '1':
		a = int(entrada[1])
		b = int(entrada[2])	
		print soma(a,b)
	
	

