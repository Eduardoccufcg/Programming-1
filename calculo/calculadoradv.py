# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Calculadora DV



numero_de_banco = raw_input()
pares = 0
impares = 0


for i in range (0,len(numero_de_banco),2):
	pares += int(numero_de_banco[i])
for k in range(1,len(numero_de_banco),2):		
	impares += int(numero_de_banco[k])
digito = impares * pares
	
if digito % 11 == 10:
	print'%s-X' % numero_de_banco
else:
	print'%s-%i' % (numero_de_banco, (digito % 11))
	
