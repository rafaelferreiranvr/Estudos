#Faça um algorítmo que calcule a área de um trapézio.
basemenor = float(input("Base menor do trapézio: "))
basemaior = float(input("Base maior do trapézio: "))
altura = float(input("Altura do trapézio: "))

if basemenor>0 and basemaior>0 and altura>0:
    area = (basemenor + basemaior)*altura/2
    print(f"Área do trapézio: {area}")
else:
    print("Não podem haver medidas negativas.")

