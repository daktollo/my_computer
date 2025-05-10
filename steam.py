from oyun import Oyun

class Steam:
    def __init__(self):
        self.oyunlar = []

    def varsayilan_oyunlari_ekle(self):
        oyun1 = Oyun("test1", 30, 4)
        oyun2 = Oyun("test2", 30, 4)
        self.oyunlar.append(oyun1)
        self.oyunlar.append(oyun2)


if __name__ == "__main__":
    steam = Steam()
    steam.varsayilan_oyunlari_ekle()

    sayac = 0
    while sayac < len(steam.oyunlar):
        print(steam.oyunlar[sayac].isim)
        sayac += 1


    for oyun in steam.oyunlar:
        print(oyun)


