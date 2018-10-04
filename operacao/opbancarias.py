# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Operações Bancárias

nome_saldo = raw_input().split()
nome, saldo_atual = nome_saldo[0], float(nome_saldo[1])

while True:
	operacao = raw_input().split()
	if operacao[0] == '3':
		break
	elif operacao[0] == '1':
		saldo_atual += float(operacao[1]) * -1
	elif operacao[0] == '2':
		saldo_atual += float(operacao[1])
print'Saldo de R$ %.2f na conta de %s' % (saldo_atual, nome)
