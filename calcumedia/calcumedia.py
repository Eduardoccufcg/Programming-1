# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Calculadora de Médias

# Funçoes Calculo de Médias

def cal_MA(valores):
	soma = 0
	for i in valores:
		soma += float(i)
	media_aritmetica = soma / len(valores)
	return media_aritmetica
def cal_MG(valores):
	multi = 1
	for i in valores:
		multi *= float(i)
	media_geometrica = multi ** (1.0 / len(valores))
	return media_geometrica
def cal_MH(valores):
	soma = 0
	for d in valores:
		x = 1/ float(d)
		soma += x
	media_harmonica = len(valores) / soma
	return media_harmonica

while True:
	check = raw_input().split()
	if check == ['Q']:
		break
	valores = raw_input().split()
	for i in range(len(check)):
		if check[i] == 'MA':
			print'Média Aritmética: %.4f' % cal_MA(valores)
		if check[i] == 'MG':
			print'Média Geométrica: %.4f' % cal_MG(valores)
		if check[i] == 'MH':
			print'Média Harmônica: %.4f' % cal_MH(valores)
	print"----"
