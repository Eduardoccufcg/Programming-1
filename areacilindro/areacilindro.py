# coding: utf-8
# Eduardo Pereira / Programação 1
import math
print'Cálculo da Superfície de um Cilindro'
print'---'
medida_diametro = float(raw_input('Medida do diâmetro? '))
medida_altura = float(raw_input('Medida da altura? '))
raio = float (medida_diametro / 2)
area = float ((2 * math.pi * raio) * (raio + medida_altura))
print'---'
print'Área calculada: %.2f' % area


