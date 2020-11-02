"""Crie uma classe Televisão e uma classe ControleRemoto que pode
controlar o volume e trocar os canais da televisão.
O controle de volume permite aumentar ou diminuir a potência do
volume de som em uma unidade de cada vez
O controle de canal também permite aumentar e diminuir o número
do canal em uma unidade, porém, também possibilita trocar para um canal
indicado também devem existir métodos para consultar o valor do volume de som
e o canal selecionado. """


class controleRemoto:
    def __init__(self):
        global volume
        volume = 1
        global canal
        canal = 1

    def aumentarVolume(self):
        global volume
        if (volume + 1) <= 100:
            volume += 1
        else:
            print("Volume Máximo.")

    def diminuirVolume(self):
        global volume
        if (volume - 1) >= 0:
            volume -= 1
        else:
            print("Mudo.")

    def aumentarCanal(self):
        global canal
        canal += 1

    def diminuirCanal(self):
        global canal
        if (canal - 1) >= 0:
            canal -= 1
        else:
            print("Canal não disponível.")

    def definirCanal(self, c):
        global canal
        canal = c


class televisao:
    def info(self):
        global volume
        global canal
        print(f"Volume: {volume}\nCanal: {canal}")


# Testes
tv1 = televisao()
controle = controleRemoto()
controle.aumentarVolume()
controle.aumentarVolume()
controle.aumentarVolume()
controle.aumentarVolume()
controle.diminuirVolume()
controle.diminuirVolume()
controle.definirCanal(10)
controle.aumentarCanal()
controle.diminuirCanal()
controle.diminuirCanal()
tv1.info()
