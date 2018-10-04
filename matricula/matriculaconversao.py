# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Conversão de matriculas

matricula = raw_input()
nova_matricula =  ''
for i in range(len(matricula)):
	if i == 0:
		nova_matricula += '1'
	elif i == 4:
		nova_matricula += matricula[4] + '0'
		
	else:
		nova_matricula += matricula[i]
	
print nova_matricula
