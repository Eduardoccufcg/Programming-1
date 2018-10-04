# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Campanha

lista_gols1 =[]
lista_gols2 =[]

for i in range(10):
	placar = raw_input()
	lista_gols1.append(placar[0])
	lista_gols2.append(placar[2])

#Campinense
gols_casa = 0
gols_fora = 0
derrota = 0
vitoria_casa = 0
vitoria_fora = 0
empate_fora = 0
empate_casa = 0
for i in range(0,len(lista_gols1),2):
	gols_casa += int(lista_gols1[i])
	if int(lista_gols1[i]) > int(lista_gols2[i]):
		vitoria_casa += 1
	elif int(lista_gols1[i]) < int(lista_gols2[i]):
		derrota += 1
	else:
		empate_casa += 1
for d in range(1,len(lista_gols2),2):
	gols_fora += int(lista_gols2[d])
	if int(lista_gols2[d]) > int(lista_gols1[d]):
		vitoria_fora += 1
	elif int(lista_gols2[d]) < int(lista_gols1[d]):
		derrota += 1
	else:
		empate_fora += 1
#Adversario

golsadv_fora = 0
golsadv_casa = 0
for casaad in range(1,len(lista_gols1),2):
	golsadv_fora += int(lista_gols1[casaad])
for foraad in range(0,len(lista_gols2),2):
	golsadv_casa += int(lista_gols2[foraad])
gols_campinense = gols_casa + gols_fora
gols_adversario = golsadv_casa + golsadv_fora
saldo = gols_campinense - gols_adversario



print'%dv, %de, %id' %((vitoria_casa + vitoria_fora),(empate_casa + empate_fora),derrota)
print'pontos: %d' % ((vitoria_casa + vitoria_fora) * 3 + (empate_casa + empate_fora) *1)
print'saldo: %d (%d pro, %d contra)'% (saldo,gols_campinense,gols_adversario)		
print'pontos em casa: %d' % (vitoria_casa * 3 + empate_casa * 1)
print'pontos fora: %d' % (vitoria_fora * 3 + empate_fora *1)

