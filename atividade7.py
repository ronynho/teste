#Um veículo trafega em uma rodovia com velocidade média de 80 km/h. Sabendo que a
#viagem teve uma duração de 1 hora e 30 minutos (1,5 h), qual foi a distância percorrida
#pelo veículo?
def distancia_percorrida(v,t):
    return v * t

velocidade = 80
tempo = 1.5
distancia_total = distancia_percorrida(velocidade, tempo)
print(distancia_total)