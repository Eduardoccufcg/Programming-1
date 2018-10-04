# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Campanha


derrotas = 0
empate = 0
pontos_casa = 0
pontos_fora = 0
saldo_contra = 0
saldo_pro = 0
vitorias = 0
for i in range(0, 10):
    placar = raw_input()
    if placar[5] == 'c':
        if int(placar[0]) > int(placar[2]):
            pontos_casa += 3
            vitorias += 1
            saldo_pro += int(placar[0])
            saldo_contra += int(placar[2])
        elif int(placar[0]) == int(placar[2]):
            pontos_casa += 1
            empate += 1
            saldo_pro += int(placar[0])
            saldo_contra += int(placar[2])
        else:
            derrotas += 1
            saldo_pro += int(placar[0])
            saldo_contra += int(placar[2])
    else:
        if int(placar[0]) < int(placar[2]):
            pontos_fora += 3
            vitorias += 1
            saldo_pro += int(placar[2])
            saldo_contra += int(placar[0])
        elif int(placar[0]) == int(placar[2]):
            pontos_fora += 1
            empate += 1
            saldo_pro += int(placar[2])
            saldo_contra += int(placar[0])
        else:
            derrotas += 1
            saldo_pro += int(placar[2])
            saldo_contra += int(placar[0])

saldo = saldo_pro - saldo_contra
pontos = pontos_casa + pontos_fora

print '%dv, %de, %dd' % (vitorias, empate, derrotas)
print 'pontos: %d' % pontos
print 'saldo: %d (%d pro, %d contra)' % (saldo, saldo_pro, saldo_contra)
print 'pontos em casa: %d' % pontos_casa
print 'pontos fora: %d' % pontos_fora
