# coding: utf-8
# Espaço em disco
# (C) 2017.2, Eduardo Pereira / UFCG, Programação 1

primeiro_usuario = raw_input()
bytes_ocupados1 = float(raw_input())
segundo_usuario = raw_input()
bytes_ocupados2 = float(raw_input())
terceiro_usuario = raw_input()
bytes_ocupados3 = float(raw_input())
bytes1_em_mb = float(bytes_ocupados1 / 1024 ** 2)
bytes2_em_mb = float(bytes_ocupados2 / 1024 ** 2)
bytes3_em_mb = float(bytes_ocupados3 / 1024 ** 2)
espaco_total = float(bytes1_em_mb + bytes2_em_mb + bytes3_em_mb)
espaco_medio = float((bytes1_em_mb + bytes2_em_mb + bytes3_em_mb) / 3)

print'SPLab - Espaço utilizado pelos usuários'
print'---------------------------------------------'
print'Nr., Usuário, Espaço Utilizado'

print'\n1, %s, %3.2f MB' % (primeiro_usuario, bytes1_em_mb)
print'2, %s, %3.2f MB' % (segundo_usuario, bytes2_em_mb)
print'3, %s, %3.2f MB' % (terceiro_usuario, bytes3_em_mb)

print'\nEspaço total ocupado: %3.2f MB' % espaco_total
print'Espaço médio ocupado: %3.2f MB' % espaco_medio

