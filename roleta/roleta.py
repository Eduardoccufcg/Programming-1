# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Roleta

numero_aposta = int(raw_input())
cor_aposta = raw_input()
numero_sorteado = int(raw_input())
cor_sorteado = raw_input()
pontos = 0
if numero_aposta == numero_sorteado and cor_aposta == cor_sorteado:
	pontos = 150
elif numero_aposta == numero_sorteado and cor_aposta != cor_sorteado:
	pontos = 100
elif cor_aposta == cor_sorteado and numero_aposta != numero_sorteado and numero_sorteado > numero_aposta:
	pontos = 80
elif cor_aposta == cor_sorteado and numero_aposta != numero_sorteado and numero_sorteado < numero_aposta:
	pontos = 100
print pontos
