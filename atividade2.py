#Um carro viaja de uma cidade A a uma cidade B, distantes 200km. Seu percurso demora
#4 horas, pois decorrida uma hora de viagem, o pneu dianteiro esquerdo furou e precisou
#ser trocado, levando 1 hora e 20 minutos do tempo total gasto. Qual foi a velocidade
#média que o carro desenvolveu durante a viagem?
def velocidade_media (d, t):
    return d / t

d1 = 200
t1 = 4
vel = velocidade_media(d1,t1)
print(vel, 'Km')