#Durante uma corrida de 100 metros rasos, um competidor se desloca com velocidade
#média de 5m/s. Quanto tempo ele demora para completar o percurso?
def tempototal(d, t):
    return d / t
distancia = 100
tempo = 5
completo= tempototal(distancia, tempo)
print(completo, "segundos")