# coding: utf-8
# Entrada de dados
# (C), Eduardo Pereira / UFCG, Programação 1
import math
x = float(raw_input('Medida do Cateto 1? '))
y = float(raw_input('Medida do Cateto 2? '))
c = math.hypot(x, y)

print 'Medida da Hipotenusa:','%.2f' % c
