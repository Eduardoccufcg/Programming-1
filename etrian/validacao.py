# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Validação de Triângulos

lado_a = int(raw_input())
lado_b = int(raw_input())
lado_c = int(raw_input())
perimetro = lado_a + lado_b + lado_c

if abs(lado_b - lado_c) < lado_a < lado_b + lado_c and abs(lado_a - lado_c) < lado_b < lado_a + lado_c and abs(lado_a - lado_b) < lado_c < lado_a + lado_b:
	print'triangulo valido. %d' % perimetro
else:
	print'triangulo invalido.'	

