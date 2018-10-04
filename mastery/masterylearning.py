# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Mastery Learning
print 'Mastery Learning'
print 'Cálculo da nota na unidade'
print
nota1 = float(raw_input('Nota? '))
nota2 = float(raw_input('Nota? '))
media_parcial  = (nota1 + nota2) / 2
penalizacao = 0.0
if nota1 > nota2:
	menor = nota1
	maior = nota2
elif nota2 > nota1:
	maior = nota2
	menor = nota1


while True:
	if media_parcial >= 6.5:
		print'Média: %.1f (aprovado)' % media_parcial
		print'Penalização: %.1f' % penalizacao
		break
	else:
		print'Média: %.1f (cursando)' % media_parcial
		print'Penalização: %.1f' % penalizacao
		print	
	nota = float(raw_input('Nota? '))
	penalizacao += 0.5
	if nota > menor:
		menor = nota
		media_parcial =  (menor + maior) / 2
print	
print'==='	
print'Notas válidas: %.1f e %.1f' % (menor, maior)
print'Média parcial na unidade: %.1f' % media_parcial			
print'Penalizações: %.1f' % penalizacao
print'Média final na unidade: %.1f' % (media_parcial - penalizacao)
