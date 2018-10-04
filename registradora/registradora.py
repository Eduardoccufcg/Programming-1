# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Caixa Registradora


def caixa_registradora(vendas,meta):
	situacao = ''
	soma = 0
	comissoes = 0
	for i in vendas:
		soma += i
		if i < 1000.0:
			comissoes += i * 0.05
		elif 1000.0 <= i < 5000.0:
			comissoes += i * 0.1
		elif i >= 5000.0:
			comissoes += i * 0.15
	if soma >= meta:
		situacao += 'Lucro'
	else:
		situacao += 'Prejuizo'
	
	return[soma,comissoes,situacao]
	
