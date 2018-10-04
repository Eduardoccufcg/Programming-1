# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Privilegia Letra


def letra_magica(clientes,letra):
	for d in range(len(clientes)):	
		for i in range(len(clientes)-1):
			if clientes[i+1][0] == letra and clientes[i][0] != clientes[i+1][0]:
				clientes[i], clientes[i+1] = clientes[i+1], clientes[i]	
				
