# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Status de uma disciplina
# Programação 1 / 2017.2

nota_1 = float(raw_input())
nota_2 = float(raw_input())
nota_3 = float(raw_input())
n_faltas = int(raw_input())
presenca =  1 - (n_faltas / 30.0)
media = (nota_1 + nota_2 + nota_3) / 3


if presenca > 0.75 and media >= 7.0:
	print 'aprovado por media'
elif presenca > 0.75 and 4 <= media < 7:
	print 'prova final'
elif presenca > 0.75 and media < 4 :
	print 'reprovado por nota'
else:
	print'reprovado por faltas'
