# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Status unidade

n_testes = int(raw_input())
soma = 0
for i in range(n_testes):
	nota = float(raw_input())
	soma += nota
media = soma / n_testes

if media >= 6.0:
	print'%.1f' % media
	print'Aluno aprovado na unidade'
else:
	if n_testes > 2:
		print'%.1f' % (media - 0.5)
		print'Aluno ainda não aprovado na unidade'
	else:
		print'%.1f' % media
		print'Aluno ainda não aprovado na unidade'
