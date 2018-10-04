# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Divisão por Subtrações

contador = 0
entrada = raw_input().split()
Dividendo = int(entrada[0])
divisor = int(entrada[1])
if Dividendo >= divisor:
	while True:

		resto = Dividendo - divisor
		print'%d - %d = %d' % (Dividendo,divisor,resto)
		contador += 1
		Dividendo = resto
		if resto < divisor:
			break
			
print'%d - %d < 0' % (Dividendo,divisor)	
print'==='
print'quociente = %d' % contador
print'resto = %d' % Dividendo
