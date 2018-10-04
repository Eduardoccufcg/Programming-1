# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Conversão binario

listabinario = [ 8,4,2,1]
binario = raw_input()
soma = 0
for i in range(len(binario)):
	a = int(binario[i]) * listabinario[i]
	soma += a
	print '%d * %d = %d' % (int(binario[i]) ,listabinario[i], a)
print '%s(2) = %d(10)' % (binario,soma)
