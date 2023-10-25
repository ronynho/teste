#Um carro, se desloca a uma velocidade de 20m/s em um primeiro momento, logo após
#passa a se deslocar com velocidade igual a 40m/s, assim como mostra o gráfico abaixo.
#Qual foi o distância percorrida pelo carro?
def distancia_percorrida(v, t):
    return v * t
velocidade_a = 20
velocidade_b = 40
tempo_a = 5
tempo_b = 15 - tempo_a

distanciatotal = distancia_percorrida(velocidade_a, tempo_a) + distancia_percorrida(velocidade_b, tempo_b)
print(distanciatotal)
