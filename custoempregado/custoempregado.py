# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Custo Empregado

salario = float(raw_input())
dias = int(raw_input())
custo_transporte_diario = float(raw_input())

# custo empregador

inss_empregador = salario * 0.08
fgts_empregador = salario * 0.12
custo_transporte = dias * custo_transporte_diario
if custo_transporte > salario * 0.06:
	custo_transporte_empregador = custo_transporte - salario * 0.06
	custo_transporte_empregado = salario * 0.06
else:
	custo_transporte_empregador = 0
	custo_transporte_empregado = 0
custo_empregador = inss_empregador + fgts_empregador + custo_transporte_empregador + salario
# custo empregado
if salario <= 1317.07:
	inss_empregado = salario * 0.08
elif 1317.07 < salario <= 2195.12:
	inss_empregado = salario * 0.09
else:
	inss_empregado = salario * 0.11
salario_liquido = salario - inss_empregado - custo_transporte_empregado
print'O salário base é R$ %.2f' % salario
print'O custo mensal para o empregador é de R$ %.2f' % custo_empregador
print'O salário líquido que o trabalhador irá receber no mês é R$ %.2f' % salario_liquido
