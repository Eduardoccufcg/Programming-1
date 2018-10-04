# coding: utf-8
# Tweets por página
# Eduardo Pereira / Programação 1

numero_de_tweets = int(raw_input())
numero_de_paginas_inteiro = numero_de_tweets / 400
tweets_perdidos = float(numero_de_tweets % 400)
porcentagem_tweets_perdidos = (tweets_perdidos / numero_de_tweets) * 100.0
print'Serão necessárias %d página(s) para visualizar os tweets.' % numero_de_paginas_inteiro
print'%.1f%% dos tweets serão perdidos.' % porcentagem_tweets_perdidos

