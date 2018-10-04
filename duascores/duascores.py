# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Organiza Array com duas cores





def separa_duas_cores(l1,cor1,cor2):
	j = 0
	for i in range(len(l1)):
		if l1[i] == cor1:
			l1[i],l1[j] = l1[j],l1[i]
			j += 1
