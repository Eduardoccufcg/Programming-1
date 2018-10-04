# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Analisa Chave
vogais = 'aeiou'
senha = raw_input()
cont = 0
segura = True
d = 0
while d < (len(senha)-2):
	if senha[d] == senha[d+1] and senha[d] == senha[d+2]:
		print'Chave insegura. 3 caracteres consecutivos iguais.'
		segura = False
		
		
	elif senha[d] in vogais:
		cont += 1
		if cont > 5:
			print 'Chave insegura. %d vogais.' % cont
			segura = False
			break
			
	d += 1		
	
if segura == True:
	print'Chave segura!'

		

