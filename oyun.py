class Oyun:
    def __init__(self, isim, depolama, ram, isletim_sistemi):
        self.isim = isim
        self.depolama = depolama
        self.ram = ram

        self.calisabilecek_sistemler = isletim_sistemi

    def __str__(self):
        return self.isim

if __name__ == "__main__":
    cs = Oyun("Counter-Strike",20, 8)
    print(cs.isim)