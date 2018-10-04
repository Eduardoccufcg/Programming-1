# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Calculo de seguro

def calcula_seguro(valor,lista):
	idade = lista[0]
	casado = lista[1]
	area_risco = lista[2]
	portao = lista[3]
	imovel = lista[4]
	casa_propria = lista[5]
	veiculo = lista[6]
	
	pontuacao = 0
	# análise idade
	if idade <= 21:
		pontuacao += 20
	elif 21 < idade <= 30:
		pontuacao += 15
	elif 30 < idade <= 40 :
		pontuacao += 12
	elif 40 < idade <= 60:
		pontuacao += 10
	elif idade > 60:
		pontuacao += 20
	# análise situaçao civil
	if casado == True:
		pontuacao += 10
	else:
		pontuacao += 20
	# análise área de risco
	if area_risco == True:
		pontuacao += 20
	else:
		pontuacao += 10
	# análise portao elettonico
	if  portao == True:
		pontuacao += 20
	else:
		pontuacao += 10
	# análise imovel
	if imovel == True:
		pontuacao += 20
	else:
		pontuacao += 10
	# análise casa própria
	if casa_propria == True:
		pontuacao += 10
	else:
		pontuacao += 20
	# análise uso do veículo
	if veiculo == 'Trabalho':
		pontuacao += 10
	elif veiculo == 'Lazer':
		pontuacao += 20
	elif veiculo == 'Misto':
		pontuacao += 20
	# análise de risco
	if pontuacao <= 80:
		risco = 'Risco Baixo'
	elif 80 < pontuacao <= 100:
		risco = 'Risco Medio'
	elif pontuacao > 100:
		risco = 'Risco Alto'
	# Valor a ser pago
	if risco == 'Risco Alto':
		valor_pago = valor * 0.3
	elif risco == 'Risco Medio':
		valor_pago = valor * 0.2
	elif risco == 'Risco Baixo':
		valor_pago = valor * 0.1
		
	return [pontuacao,risco,valor_pago]


	
	
