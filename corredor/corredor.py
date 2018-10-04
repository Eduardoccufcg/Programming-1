# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Classifica Corredor

quantidade_km = float(raw_input())
tempo = float(raw_input())
velocidade_media = quantidade_km / tempo

if velocidade_media < 10.0:
	print 'Velocidade: %.1fkm/h. Corredor amador.' % velocidade_media
elif 10.0 <= velocidade_media <= 15.0:
	print 'Velocidade: %.1fkm/h. Corredor aspirante.' % velocidade_media
else:
	print 'Velocidade: %.1fkm/h. Corredor profissional.' % velocidade_media
