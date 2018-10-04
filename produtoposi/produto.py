# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Produto de dois somatórios

numero = raw_input()
soma_par = 0
soma_impar = 0
for c in range(len(numero)):
	if c == 2 or c == 4 or c == 0:
		soma_par += int(numero[c])
		
	else:
		soma_impar += int(numero[c])

produto = soma_par * soma_impar

if len(str(produto)) == 1:
	print '0000'+str(produto)
elif len(str(produto)) == 2:
	print '000'+str(produto)
elif len(str(produto)) == 3:
	print '00'+str(produto)
elif len(str(produto)) == 4:
	print '0'+str(produto)	


