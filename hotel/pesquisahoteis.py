# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Pesquisa Hóteis

lista_valor = []
lista_tamanho = []
lista_conforto = []
lista_empresa = []
while True:
	entradas = raw_input().split(',')
	if entradas[0] ==  '---':
		break
	else:
		valor, tamanho, conforto, empresa  = entradas[0], entradas[1],entradas[2], entradas[3]
		lista_valor.append(valor)
		lista_tamanho.append(tamanho)
		lista_conforto.append(conforto)
		lista_empresa.append(empresa)
			
menor = float(lista_valor[0])
maior = int(lista_tamanho[0])
maior_conforto = int(lista_conforto[0])
while True:
	pesquisa = raw_input()
	if pesquisa == 'fim':
		break
	elif pesquisa == 'valor':
		for d in range(len(lista_empresa)):
			if float(lista_valor[d]) < menor:
				menor -= menor
				menor += float(lista_valor[d])
				empresa_menor = ''
				empresa_menor += lista_empresa[d]
			elif float(lista_valor[d]) == menor:
				menor -= menor
				menor += float(lista_valor[d])
				empresa_menor = ''
				empresa_menor += lista_empresa[d]
				
		print empresa_menor
		
	elif pesquisa == 'tamanho':
		for d in range(len(lista_empresa)):
			if float(lista_tamanho[d]) > maior:
				maior -= maior
				maior += int(lista_tamanho[d])
				empresa_maior = ''
				empresa_maior += lista_empresa[d]
			elif float(lista_tamanho[d]) == maior:
				maior -= maior
				maior += int(lista_tamanho[d])
				empresa_maior = ''
				empresa_maior += lista_empresa[d]
				
		print empresa_maior
		
	elif pesquisa == 'conforto':
		for d in range(len(lista_empresa)):
			if float(lista_conforto[d]) > maior_conforto:
				maior_conforto -= maior_conforto
				maior_conforto += int(lista_conforto[d])
				empresa_maior_conforto = ''
				empresa_maior_conforto += lista_empresa[d]
				
			elif float(lista_conforto[d]) == maior_conforto:
				maior_conforto -= maior_conforto
				maior_conforto += int(lista_conforto[d])
				empresa_maior_conforto = ''
				empresa_maior_conforto += lista_empresa[d]
		print empresa_maior_conforto

