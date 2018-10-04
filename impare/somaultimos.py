# coding: utf -8
# Soma dos ultimos ímpares
# Eduardo Pereira dos Santos / Programação 1 / Matricula: 117210342

n_quantidades = int(raw_input())
limite = int(raw_input())

lista_numero = []
for d in range(n_quantidades):
	numeros_sequencia = int(raw_input())
	lista_numero.append(numeros_sequencia)

soma = 0	
for numero in range(len(lista_numero)-1,-1,-1):
	if lista_numero[numero] % 2 != 0:
		if soma + lista_numero[numero] < limite:
			soma += lista_numero[numero]
		else:
			break
print soma

	
		
		

	
