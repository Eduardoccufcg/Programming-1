# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Ataque mais positivo

somatorio = 0
gols = 0
melhor_time = ''

n_times = int(raw_input())

for i in range(n_times):
	
	nome_time = raw_input()
	gols_time = int(raw_input())
	somatorio += gols_time   
	if gols_time > gols:
		gols -= gols
		gols += gols_time
		melhor_time = ''
		melhor_time += nome_time + '\n'
	elif gols_time == gols:
		gols -= gols
		gols += gols_time
		melhor_time += nome_time + '\n'
   

print'Time(s) com melhor ataque (%d gol(s)):' % gols
print'%s' % melhor_time
print'Média de gols marcados: %.1f' % (somatorio / float(n_times))

