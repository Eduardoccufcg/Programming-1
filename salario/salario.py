#coding: utf-8
# (c) 2017, Eduardo Pereira, UFCG, Programação 1
salario_bruto = float(raw_input())
horas_de_trabalho = int(raw_input())
horabruta = salario_bruto / horas_de_trabalho
des_ir = float(salario_bruto * 11/100)
des_inss = float(salario_bruto * 8/100)
des_sin = float(salario_bruto* 5/100)
salarioliqui = float(salario_bruto-des_ir-des_inss-des_sin)
horaliquida = float(salarioliqui / horas_de_trabalho)
print'Salário Bruto =',salario_bruto
print'Hora Bruta =' ,horabruta
print'Desconto IR =' ,des_ir
print'Desconto INSS =' ,des_inss
print'Desconto Sindicato =',des_sin
print'Salário Líquido =',salarioliqui
print'Hora Líquida =' ,horaliquida


