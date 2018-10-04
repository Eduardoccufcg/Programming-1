# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Transporte modificado

n_pessoas = int(raw_input())
valor_em_reais = float(raw_input())

if valor_em_reais < 22:
	print'Não é possível realizar a viagem.'
else: 
	valor_por_pessoa = valor_em_reais / n_pessoas
	if valor_por_pessoa < 22:
	   print'Não é possível realizar a viagem.'
	else:
		custo_tav = 100 * n_pessoas
		custo_onibus = 22 * n_pessoas
		if n_pessoas % 4 == 0:
			custo_taxi = 200 * (n_pessoas / 4)
		else:
			custo_taxi = 200 * (n_pessoas / 4) + 200
	
		if custo_tav <= valor_em_reais:
			print'TAV. R$ %.2f' % custo_tav
		elif custo_taxi <= valor_em_reais:
			print'Táxi. R$ %.2f' % custo_taxi
		else: 
			print'Ônibus. R$ %.2f' % custo_onibus

