# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Peso Ideal com Função

def calculaPeso(sexo,altura):
		if sexo == 'f' or sexo == 'F':
			pesoideal = 62.1 * altura - 44.7 
			print'Mulher: peso ideal é %.1f' % pesoideal
		if sexo == 'm' or sexo == 'M':
			pesoideal = 72.7 * altura - 58.0
			print'Homem: peso ideal é %.1f' % pesoideal

while True:	
	entrada = raw_input().split()
	if entrada[0] == '****':
		break
	sexo = entrada[0]
	altura = float(entrada[1])
	calculaPeso(sexo,altura)
