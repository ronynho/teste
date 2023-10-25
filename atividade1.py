#Escreva uma função em Python para os seguintes problemas:

#Um macaco que pula de galho em galho em um zoológico, demora 6 segundos para
#atravessar sua jaula, que mede 12 metros. Qual a velocidade média dele?
def velocidade_media (d, t):
    return d / t

d1 = 12
t1 = 6
vel = velocidade_media(d1,t1)
print(vel,'m/s')