# coding: utf-8
# Percentual de Reajuste
# Eduardo Pereira / Programação 1
valor_salario = float(raw_input('Valor atual? '))
novo_valor = float(raw_input('Novo valor? '))
reajuste = float(((novo_valor / valor_salario ) - 1) * 100 )
print 'Reajuste de %.1f%%' % reajuste

