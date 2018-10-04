# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Z Inicial

def z_inicial(lista):
	cont_z = 0
	for d in range(len(lista)):
		if lista[d][0] == 'z' or lista[d][0] == 'Z':
			cont_z += 1
	return cont_z
	
nomes = raw_input().split()
print(z_inicial(nomes))
