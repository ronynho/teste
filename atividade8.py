#Um veículo automotivo acelera a 2,0 m/s², durante 5,0 s, a partir de uma velocidade
#inicial de 2,0 m/s. A distância percorrida por esse veículo, durante esse intervalo de
#tempo, é igual a?
def distancia_percorrida(v,t):
    return v * t
tempo = 5.0
velocidade_inicial = 2
aceleração = 2
velocidade_final = tempo * aceleração + velocidade_inicial
media_velocidade = (velocidade_inicial + velocidade_final) / 2
percorrida_total = distancia_percorrida(media_velocidade, tempo)
print(percorrida_total)
