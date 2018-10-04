# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Já sei tocar essa musica

def sei_tocar_musica(musica,acordes):
	sei = 0
	for d in range(len(musica)):
		for j in range(len(acordes)):
			if musica[d] == acordes[j]:
				sei += 1
	if sei == len(musica):
		return True
	else:
		return False
