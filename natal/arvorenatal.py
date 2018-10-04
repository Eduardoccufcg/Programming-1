# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: arvore de natal

altura_arvore = int(raw_input())
num_espacos = altura_arvore - 1
multiplica = 1
for c in range(altura_arvore):
	arvore = multiplica * 'o'
	print num_espacos * ' ' + arvore
	num_espacos -=1
	multiplica +=2
print (altura_arvore-1) * ' ' + 'o'
