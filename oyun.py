class Oyun:
    def __init__(self, isim, depolama, ram):
        self.isim = isim
        self.depolama = depolama
        self.ram = ram


if __name__ == "__main__":
    cs = Oyun("Counter-Strike",20, 8)
    print(cs.isim)
    print(cs.depolama)
    print(cs.ram)