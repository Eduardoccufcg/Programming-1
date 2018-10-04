# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Dígito de verificacao CPF

entrada = ''
def calcula_digitos_verificacao(entrada):
	soma = 0
	for i in range(len(entrada) -1 ,-1,-1):
		multi = (len(entrada) - i + 1) * int(entrada[i])
		soma += multi
	digito = str(soma * 10 % 11)
	if digito == '10':
		digito = '0'
	entrada2 = entrada + str(digito)
	soma2 = 0
	for i in range(len(entrada2) -1 ,-1,-1):
		multi2 = (len(entrada) - i + 2) * int(entrada2[i])
		soma2 += multi2
	digito2 = str(soma2 * 10 % 11)
	if digito2 == '10':
		digito2 = '0'
	return(digito + digito2)

