# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Autorização_voos
soma = 0
voos = 0

tempo_disponivel = int(raw_input())
numero_avioes = int(raw_input())

lista = []
for i in range(numero_avioes):
		tempo_aviao = int(raw_input())
		lista.append(tempo_aviao)
for d in lista:
	if d <= tempo_disponivel:
		soma += d
		if soma <= tempo_disponivel:
			voos += 1
print'%d voo(s) autorizados.' % voos
	 
