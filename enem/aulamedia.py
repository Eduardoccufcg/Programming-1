# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Aula de Médias

lista_de_notas = []
soma = 0
quantidades_notas = 0
while True:
	notas = raw_input()
	lista_de_notas.append(notas)
	soma += float(notas)
	quantidades_notas += 1
	if soma >= 100.0:
		break
		
media = soma / quantidades_notas	
print'Quantidade de numeros lidos: %d' %  quantidades_notas
print'Soma dos numeros lidos: %.2f' %  soma
print'Média = %.2f' % media

print'\nAbaixo da média'	
for i in range(len(lista_de_notas)):
	if float(lista_de_notas[i]) < media:
		print'%.2f (%do)' % (float(lista_de_notas[i]), i+1)
print'\nAcima da média'
for i in range(len(lista_de_notas)):
	if float(lista_de_notas[i]) > media:
		print'%.2f (%do)' % (float(lista_de_notas[i]), i+1)
