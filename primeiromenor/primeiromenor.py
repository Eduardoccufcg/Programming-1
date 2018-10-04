# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Primeiro Menor

def primeiro_menor(num,numeros):
	tem_menor = False
	for i in range(len(numeros)):
		if int(numeros[i]) < num:
			indice = i
			tem_menor = True
			break 
	if tem_menor == False:
		indice = -1
	return indice

def main():
	numeros = raw_input().split()
	num = int(raw_input())
	
	if primeiro_menor(num,numeros) != -1:
		print 'primeiro menor que %d: %d' % (num , int(numeros[primeiro_menor(num,numeros)]))
	else:
		print 'sem menores que %d' % num

if __name__ == '__main__':
    main()
