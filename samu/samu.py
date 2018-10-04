# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Atendimento no Samu

soma_atendimentos = 0
lista_atendimentos = []
for m in range(12):
	n_atendimentos_mes = int(raw_input())
	lista_atendimentos.append(n_atendimentos_mes)
	soma_atendimentos += n_atendimentos_mes

media_mensal = soma_atendimentos / 12.0
print'Média mensal de atendimentos: %.2f' % media_mensal
print'----'

for d in range(len(lista_atendimentos)):
	if lista_atendimentos[d] > media_mensal:
		print 'Mês %d: %d' % (d+1,lista_atendimentos[d])
	
