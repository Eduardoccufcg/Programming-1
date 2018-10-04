# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Números Oscilantes


codigo = int(raw_input())
codigo = str(codigo)

for d in range(len(codigo) -1 ):
	codigo_1 = True
	if int(codigo[d]) % 2 == int(codigo[d+1]) % 2:
		codigo_1 = False
		break
if codigo_1 == True:
	print'verdadeiro: %d algarismos.' % len(str(codigo))
else:
	print'falso: %d algarismos.' % len(str(codigo))
