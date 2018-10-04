# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Cria Senha


def criaSenhaFraca(palavra):
	senha = ''
	for caractere in palavra:
		if caractere == 'o' or caractere == 'O':
			senha += '0'
		elif caractere == 'i' or caractere == 'I' or caractere == 'L' or caractere =='l':
			senha += '1'
		elif  caractere == 'e' or caractere == 'E':
			senha += '3'
		elif caractere == 'a' or caractere == 'A':
			senha += '4'
		elif caractere == 'b' or caractere == 'B':
			senha += '6'
		elif caractere == 't' or caractere == 'T':
			senha += '7'
		else:
			senha += caractere
	return senha

while True:
	comando = raw_input().split()
	if comando == ['***']:
		break
	palavra = comando[0]
	if comando[1] == 'fraco':
		print'((%s))' % palavra
	else:
		print'((%s))' % criaSenhaFraca(palavra)
