# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Análise de Variação do Salário Mínimo

ano_inicial = int(raw_input())
ano_final = int(raw_input())
salario_base = 100.00
anos = 0 
lista_salario = []

for salario in range(ano_inicial,ano_final+1):
	salario_minimo = float(raw_input())
	anos += 1
	lista_salario.append(salario_minimo)
abaixo = 0
acima = 0
soma_abaixo = 0
soma_acima = 0
for i in lista_salario:
	if i < salario_base:
		abaixo += 1
		soma_abaixo += i
	else:
		acima += 1
		soma_acima += i

print'%d ano(s) abaixo (%0.f%% dos anos)' % (abaixo, abaixo * 100.0 / anos)		
if abaixo != 0:
	print'média dos anos abaixo: U$ %.2f' % (soma_abaixo / abaixo)
print'%d ano(s) acima (%0.f%% dos anos)' % (acima, acima * 100.0 / anos)			
if acima != 0:
	print'média dos anos acima: U$ %.2f' % (soma_acima / acima)

	

	
