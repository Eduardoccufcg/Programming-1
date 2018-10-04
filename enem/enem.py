# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: AAprovados no Enem

lista_nomes = []
lista_notas = []

while True:
	entrada = raw_input().split()
	if entrada == ['fim']:
		break
	nome , nota = entrada[0] , int(entrada[1])
	lista_nomes.append(nome)
	lista_notas.append(nota)

nota_corte = int(raw_input())

nao_aprovados = 0
for i in range(len(lista_nomes)):
	if lista_notas[i] >= nota_corte:
		print '%s, %d' % (lista_nomes[i],lista_notas[i])
	else:
		nao_aprovados += 1 
		
if nao_aprovados == len(lista_nomes):
	print 'Nenhum candidato aprovado.'

