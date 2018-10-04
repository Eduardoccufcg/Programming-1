# coding: utf-8
# Porcentagem de Aprovados
# (C) 2017.2, Eduardo Pereira / UFCG, Programação 1
print'Análise da Turma'
print'==='
aprovados = int(raw_input('Número de aprovados? ')) 
reprovados = int(raw_input('Número de reprovados? '))
total = float(aprovados + reprovados)
aprovadospor = float(aprovados / total) * 100 
reprovadospor = float(reprovados / total) * 100
print'---'
print 'Total de alunos na turma:',int(total)
print 'Aprovados:', aprovados ,'= %.1f%%' % (aprovadospor)
print 'Reprovados:', reprovados, '= %.1f%%' % (reprovadospor)

