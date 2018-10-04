# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Insere na Posição Indicada



l = [10,20,30]

a_inserir = [(5,1), (-2,4),(0,0)]


for d  in range(len(l)):
	l.append(a_inserir[d][0])
	i = len(l)
	while i == a_inserir[d][1]:
		l[i],l[i-1] = l[i-1],l[i]
		i -= 1

print l			
