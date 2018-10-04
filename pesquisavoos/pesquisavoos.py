# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342 / UFCG / PROGRAMAÇAO 1
# Atividade: Pesquisa Voos

lista_valor = []
lista_conexao = []
lista_tempo = []
lista_empresa = []
n = int(raw_input())
for i in range(n):
	entradas = raw_input().split(',')
	lista_valor.append(entradas[0])
	lista_conexao.append(entradas[1])
	lista_tempo.append(entradas[2])
	lista_empresa.append(entradas[3])

cia_valor = lista_empresa[0]
cia_conexao = lista_empresa[0]
cia_tempo = lista_empresa[0]
	
menor_valor = float(lista_valor[0])
menor_conexao = int(lista_conexao[0])
menor_tempo = int(lista_tempo[0])

for d in range(len(lista_empresa)):
		
	if menor_valor > float(lista_valor[d]):
		menor_valor = float(lista_valor[d])
		cia_valor = lista_empresa[d]
		
	elif menor_valor == float(lista_valor[d]):
		menor_valor = menor_valor
		cia_valor =	cia_valor
		
	if menor_conexao > int(lista_conexao[d]):
		menor_conexao = int(lista_conexao[d])
		cia_conexao = lista_empresa[d]
	elif menor_conexao == int(lista_conexao[d]):
		menor_conexao = menor_conexao
		cia_conexao = cia_conexao
		
	if menor_tempo > int(lista_tempo[d]):
		menor_tempo = int(lista_tempo[d])
		cia_tempo = lista_empresa[d]
	elif menor_tempo == int(lista_tempo[d]):
		menor_tempo = menor_tempo
		cia_tempo = cia_tempo
			
while True:
	pesquisa = raw_input()
	if pesquisa == 'fim':
		break
	elif pesquisa == 'valor':
		print cia_valor	
				
	elif pesquisa == 'conexões':
		print cia_conexao
				
	elif pesquisa == 'tempo':
		print cia_tempo
	
