"""Faça um programa para leia o horário (hora, minuto e segundo) de inicio e a duração, em segundos, de uma experiência biológica. 
O programa deve resultar com o novo horário (hora, minuto e segundo) do termino da mesma. """
s = 0
m = 0
h = 0


duracao = input("Digite a hora de início do experimento (formato s, min, h): ")
segundos = int(input("Digite a duração da experiência em segundos: "))


duracao = duracao.split(", ")
for x in range(len(duracao)):
    duracao[x] = int(duracao[x])
try:
    m = duracao[1]
except:
    pass
try:
    h = duracao[2]
except:
    pass


horas = (segundos // 3600) + h
minutos = ((segundos % 3600) // 60) + m
segundos = ((segundos % 3600) % 60) + s
print(f"Hora do fim da experiência: {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")