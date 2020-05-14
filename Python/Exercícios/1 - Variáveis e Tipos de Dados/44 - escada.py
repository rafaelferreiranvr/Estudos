""" Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. 
Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo. """
altescada = float(input("Altura desejada: "))
altdegrau = float(input("Altura de cada degrau: "))
degraus = altescada/altdegrau
degrauincompleto = degraus % 1 
if degrauincompleto % 1 != 0:
    degraus += (1 - degrauincompleto)
    print(f"Degraus: {degraus} ")
else:
    print(f"Degraus: {degraus} ")
    
    