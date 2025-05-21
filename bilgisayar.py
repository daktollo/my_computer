from steam import Steam

class Bilgisayar:
    def __init__(self, isletim_sistemi, depolama, ram):
        self.katalog = Steam()
        self.katalog.varsayilan_oyunlari_ekle()
        self.isletim_sistemi = isletim_sistemi
        self.depolama = depolama
        self.ram = ram

bilgisayar1 = Bilgisayar("windows", 500, 16)
print(bilgisayar1.ram)
print(bilgisayar1.katalog.oyunlar)
