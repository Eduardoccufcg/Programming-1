# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Quem acertou menos

aluno_que_errou_mais = 0
maior_erro = 0
erros = 0
aluno = 1
n_resultados = int(raw_input())

for i in range(n_resultados):
	resultado_aluno = raw_input()
	for d in resultado_aluno:
		if d == 'f':
			erros += 1
	
	if erros > maior_erro:
		maior_erro = erros
		aluno_que_errou_mais = aluno
	erros = 0
	aluno += 1
print 'O aluno %d errou %d teste(s).' % (aluno_que_errou_mais,maior_erro)
		




