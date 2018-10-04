# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Descarta facilmente

n = int(raw_input())
descartados =[]
aceitos = []
for c in range(n):
	numero = raw_input()
	aceito = False
	for i in range(len(numero)):
		if i == int(numero[i]):
			aceito = True
			descartados.append(numero)
			break
	if aceito == False:
		aceitos.append(numero)
		
print'---'
print'%d aceito(s)' % len(aceitos)
for i in aceitos:
	print i			
print'%d descartado(s)' % len(descartados)
for d in descartados:
	print d

