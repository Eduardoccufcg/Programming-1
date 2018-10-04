# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: DNA

sequencia1 = raw_input()
sequencia2 = raw_input()
sequencia3 = raw_input()

if len(sequencia1) == len(sequencia2) and len(sequencia1) < len(sequencia3) and len(sequencia2) < len(sequencia3):
	print sequencia1 , len(sequencia1)
elif len(sequencia1) == len(sequencia3) and len(sequencia1) < len(sequencia2) and len(sequencia3) < len(sequencia2):
	print sequencia1 , len(sequencia1)
elif len(sequencia2) == len(sequencia3) and len(sequencia2) < len(sequencia1) and len(sequencia3) < len(sequencia1): 
	print sequencia2 , len(sequencia2)
elif len(sequencia1) == len(sequencia2) and len(sequencia3) == len(sequencia2):
	print sequencia1, len(sequencia1)

elif len(sequencia1) < len(sequencia2) and len(sequencia1) < len(sequencia3):
	print sequencia1, len(sequencia1)
elif len(sequencia2) < len(sequencia1) and len(sequencia2) < len(sequencia3):
	print sequencia2, len(sequencia2)
elif len(sequencia3) < len(sequencia1) and len(sequencia3) < len(sequencia2):
	print sequencia3 , len(sequencia3)



