from steam import Steam
from oyun import Oyun

class Bilgisayar:
    def __init__(self, isletim_sistemi, depolama, ram):
        self.katalog = Steam()
        self.katalog.varsayilan_oyunlari_ekle()
        self.isletim_sistemi = isletim_sistemi
        self.depolama = depolama
        self.ram = ram

    def calisir_mi(self, oyun):
        if oyun.ram > self.ram or oyun.depolama > self.depolama or self.isletim_sistemi not in  oyun.calisabilecek_sistemler:
            print(f"{oyun.isim} yüklenemedi")
        else:
            print(f"{oyun.isim} başarıyla yüklendi")

bilgisayar1 = Bilgisayar("linux", 500, 16)
print(bilgisayar1.ram)
print(bilgisayar1.katalog.oyunlar[0])


test_oyunu = Oyun("Minecraft", 30, 8, ["linux", "windows"])
bilgisayar1.calisir_mi(test_oyunu)

