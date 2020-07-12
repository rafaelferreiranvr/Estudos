#Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos. 
segundos = int(input("Digite o tempo em segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = (segundos % 3600) % 60
print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")