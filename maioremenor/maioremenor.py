# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Maiores e Menores

lista_menores = []
lista_maiores = []

pivot = int(raw_input())

while True:
	numero = int(raw_input())
	if numero < 0:
		break
	if numero <= pivot:
		lista_menores.append(numero)
	else:
		lista_maiores.append(numero)

print lista_menores
print pivot
print lista_maiores
