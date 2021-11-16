

class Onlisans(Ogrenci):
    def __init__(self,ad,soyad,ogrno,bolum):
        Ogrenci.__init__(self,ad,soyad,ogrno)
        self.bolum = bolum
    def BilgiYaz(self):
        print(self.ogrno + " " + self.ad + " " + self.soyad + self.bolum)
