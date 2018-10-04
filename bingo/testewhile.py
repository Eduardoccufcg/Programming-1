# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Bingo


cartela1 = raw_input()
cartela2 = raw_input()
sorteio1 = 0
sorteio2 = 0
while sorteio1 < 4 and sorteio2 < 4:
	numero_sorteado = raw_input()
	for d in range(len(cartela1)):
		if numero_sorteado == cartela1[d]:
			sorteio1 +=1
		if numero_sorteado == cartela2[d]:
			sorteio2 += 1
			
if sorteio1 < sorteio2:
	print'Bingo! Jogador 2 venceu.'
	
elif sorteio1 > sorteio2:
	print'Bingo! Jogador 1 venceu.'
else:
	print'Empate.'
		
