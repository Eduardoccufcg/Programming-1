# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Fatorial

n = int(raw_input())

resultado = 1
soma = 0
lista = range(1,n+1)

for x in lista:
	resultado = x * resultado
print resultado

