# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Pedágio

veiculo = raw_input()

if veiculo == 'Ônibus' or veiculo == 'Caminhão' or veiculo == 'Automóvel utilitário' or veiculo == 'Motocicleta':
	if veiculo == 'Ônibus':
		eixos = int(raw_input())
		onibus = 11.40 * eixos
		print'Valor a pagar: R$ %.2f.' % onibus
	elif veiculo == 'Caminhão':	
		eixos = int(raw_input())
		caminhao = 9.60 * eixos
		print'Valor a pagar: R$ %.2f.' % caminhao
	elif veiculo == 'Automóvel utilitário':
		automovel_utilitario = 11.40
		print 'Valor a pagar: R$ %.2f.' % automovel_utilitario
	elif veiculo == 'Motocicleta':
		motocicleta = 5.70
		print'Valor a pagar: R$ %.2f.' % motocicleta      		
else:
	print'Veículo não cadastrado.'

