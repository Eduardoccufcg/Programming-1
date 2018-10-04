# coding: utf-8
base = int(raw_input())
altura = int(raw_input())

perimetro = float(2*(base + altura))
perimetro_cm = float(perimetro/10)
print 'O perímetro resultante (em cm) é %.2f.' % perimetro_cm
