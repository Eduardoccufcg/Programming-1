# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Sistema de Metas de Venda Mensal

venda_mensal = float(raw_input())
meta_mensal = venda_mensal / 6

soma = 0
lista_vendas = []
meta_nao_atingida = 0
for vendas in range(6):
	vendas_funcionarios = float(raw_input())
	soma += vendas_funcionarios
	if vendas_funcionarios >= meta_mensal:
		lista_vendas.append(vendas_funcionarios)
	else:
		meta_nao_atingida += 1


if meta_nao_atingida == 0:
	print'Total de vendas: R$ %.2f (meta atingida)' % soma
	print'----'
	print'Bonificação:'
	for d in range(len(lista_vendas)):
		print'Funcionário %d: R$ %.2f' % (d+1,lista_vendas[d] * 0.01)
else:	
	print'Total de vendas: R$ %.2f (meta não foi atingida)' % soma
	print'----'

	

			
		
