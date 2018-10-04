# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Letras coincidentes

palavra_1 = raw_input()
palavra_2 = raw_input()

soma2 = 0

for i in palavra_2:
	soma2 += 1

for i in palavra_1:
	soma2 +=1
soma = 0 
print'Letras coincidentes'
for i in range (len(palavra_1)):
	
	if palavra_1[i] == palavra_2[i]:
		soma += 1
		print "'%s' na posição %d" %  (palavra_1[i],i+1)
		
print"Total de letras coincidentes: %d (%.0f%%)" % (soma, float(soma) * 100 / soma2) 
