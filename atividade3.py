#Um bola de basebol é lançada com velocidade igual a 108m/s, e leva 0,6 segundo para
#chegar ao rebatedor. Supondo que a bola se desloque com velocidade constante. Qual a
#distância entre o arremessador e o rebatedor?
def distancia (v, t):
    return v * t

v = 108
t = 0.6
d_total = distancia(v,t)
print(d_total)