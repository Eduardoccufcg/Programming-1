# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Caixa Alta

def caixa_alta(A):
	frase = ''
	nova_palavra = ''
	lista = []
	nova = ''
	A = A + ' '
	for d in range(len(A)):
		if A[d] != ' ':
			nova += A[d]
		else:
			lista.append(nova)
			nova = ''
	if len(A) == 1:
		for i in A:
			nova_palavra += i.lower()
	else:
		for j in range(len(lista)):
			nova_palavra = ''
			palavra = lista[j]
			if len(palavra) == 1:
				nova_palavra += palavra.lower()
			else:
				for h in range(len(palavra)):
					if h == 0:
						nova_palavra += palavra[h].upper()
					else:
						nova_palavra += palavra[h]
			if j != len(lista) - 1:
				frase += nova_palavra + ' '
			else:
				frase += nova_palavra					
				
				
	return frase


