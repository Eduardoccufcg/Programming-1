# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Custo INSS

salario = float(raw_input())

inss_empregador = salario * 0.12
inss_empregado_8 = salario * 0.08
inss_empregado_9 = salario * 0.09
inss_empregado_11 = salario * 0.11

if salario <= 1317.07:
	print 'O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f' % inss_empregador
	print 'O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f' % inss_empregado_8

elif salario >= 1317.08 and salario <= 2195.12:
	print 'O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f' % inss_empregador
	print 'O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f' % inss_empregado_9
	
else:
	print 'O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f' % inss_empregador
	print 'O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f' % inss_empregado_11
	
	
