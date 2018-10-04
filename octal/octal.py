# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Octal / Decimal

octal = raw_input()

soma = 0
for i in range(len(octal)):
	bit = int(octal[i])
	expoente = len(octal) - 1 -i 
	base = 8
	valor = 8 ** expoente
	total = bit * valor
	soma += total
	print '%d * %d^%d = %d' % (bit,base,expoente,total)

print'%s(8) = %d(10)' % (octal,soma)
