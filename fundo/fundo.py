# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Fundo de Investimento

media = 0
soma = 0
contador = 0


while True:
	contador += 1
	valor = float(raw_input())
	if valor < media:
		break
	soma += valor
	media = soma / contador
print'Saldo total do FIS: R$%.2f.' % soma	
print'Média das contribuições: R$%.2f.' % (soma /(contador - 1))
