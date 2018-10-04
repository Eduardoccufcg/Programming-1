# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Criptografando uma senha
trocas = 0
palavra_a_ser_convertida = raw_input()
palavra_convertida = ''
palavra_convertida += palavra_a_ser_convertida[0]

for caractere in range(1,len(palavra_a_ser_convertida)):
	if palavra_a_ser_convertida[caractere] == 'a' or palavra_a_ser_convertida[caractere] == 'A':
		palavra_convertida += '4'
		trocas += 1
	elif palavra_a_ser_convertida[caractere] == 'e' or palavra_a_ser_convertida[caractere] == 'E':
		palavra_convertida += '3'
		trocas += 1
	elif palavra_a_ser_convertida[caractere] == 'i' or palavra_a_ser_convertida[caractere] == 'I':
		palavra_convertida += '1'
		trocas += 1
	elif palavra_a_ser_convertida[caractere] == 'o' or palavra_a_ser_convertida[caractere] == 'O':
		palavra_convertida += '0'
		trocas += 1
	else:
		palavra_convertida += palavra_a_ser_convertida[caractere]
		
print '%s (%d troca(s))' % (palavra_convertida,trocas)

