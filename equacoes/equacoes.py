# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Corrigindo Equações
import math
coeficiente_a = int(raw_input())
coeficiente_b = int(raw_input())
coeficiente_c = int(raw_input())

delta = coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_c


if delta > 0:
	x2 = (-coeficiente_b - math.sqrt(delta)) / (2 * coeficiente_a)
	x1 = (-coeficiente_b + math.sqrt(delta)) / (2 * coeficiente_a)
	print'x1 = %.2f' % x1
	print'x2 = %.2f' % x2	
elif delta == 0:
	x = (-coeficiente_b + math.sqrt(delta)) / (2 * coeficiente_a)
	print'x = %.2f' % x
else:
	print'sem raizes reais'


