# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Verifica Operações Extrato

limite = int(raw_input())
saldo_atual = float(input())
saque = 0
while True:
	entrada = raw_input().split()
	
	if entrada[0] == 'depósito':
		if float(entrada[1]) > 1000.00:
			print'Operação inválida: %s.' % (entrada[0] + ' ' + entrada[1])
			print'Seu saldo é R$ %.2f.' % saldo_atual
			break
		else:
			saldo_atual += float(entrada[1])
	if entrada[0] == 'saque':
		if saldo_atual + float(entrada[1]) * -1 < 0:
			print'Operação inválida: %s.' % (entrada[0] + ' ' + entrada[1])
			print'Seu saldo é R$ %.2f.' % saldo_atual
			break
		else:
			saque += 1
			if saque > limite:
				print'Operação inválida: %s.' % (entrada[0] + ' ' + entrada[1])
				print'Seu saldo é R$ %.2f.' % saldo_atual
				break
			else:
				saldo_atual += float(entrada[1]) * -1
	
	
			
	
