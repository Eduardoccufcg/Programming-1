# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Aprovados e Reprovados

#coding utf -8
n_alunos = int(raw_input())
reprovados = 0
aprovados = 0
soma_aprovados = 0
soma_reprovados = 0
lista_alunos = []
for n in range(n_alunos):
	notas_alunos = raw_input()
	lista_alunos.append(notas_alunos)
	
for i in range(len(lista_alunos)):
	if float(lista_alunos[i]) >= 7.0:
		soma_aprovados += float(lista_alunos[i])
		aprovados += 1
	else:
		soma_reprovados += float(lista_alunos[i])
		reprovados += 1
			
			
print'Reprovados: %d' % reprovados
if reprovados != 0:
	print 'Média: %.1f' % (soma_reprovados / (reprovados))
print			
print'Aprovados: %d' % aprovados
if aprovados != 0:
	print 'Média: %.1f' % (soma_aprovados / (aprovados))
