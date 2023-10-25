#Dois trens partem simultaneamente de um mesmo local e percorrem a mesma trajetória
#retilínea com velocidades, respectivamente, iguais a 300km/h e 250km/h. Há
#comunicação entre os dois trens se a distância entre eles não ultrapassar 10km. Depois de
#quanto tempo após a saída os trens perderão a comunicação via rádio?
def tempo_perdido(d, v1, v2):
    v_relativa = (v1 - v2)
    tempo = d/ v_relativa
    return tempo * 60
v1 = 300
v2 = 250
d = 10
tempo_perda= tempo_perdido(d, v1, v2)
print(tempo_perda)