import random
class MP3Calar():
    def __init__(self,sarkiListesi=[]):
        if len(sarkiListesi) == 0:
            self.suanCalanSarki=" "
        if len(sarkiListesi) > 0:
            self.suanCalanSarki=sarkiListesi[secim -1]
        self.ses=100
        self.sarkiListesi=sarkiListesi
        self.durum = True
    def sarkiSec(self):
        if len(self.sarkiListesi) > 0:
            for sarki in self.sarkiListesi:  
                sayac= 1
                print("{}){}".format(sayac, sarki))
                sayac +=1
            global secim
            secim=int(input("Şarkı Numarasını Seçiniz 1 - {}: ".format(len(self.sarkiListesi))))
            while secim < 1 or secim > len(self.sarkiListesi):
                secim=int(input("Çalınacak şarkının numarasını doğru giriniz : (1-{})".format(len(self.sarkiListesi))))
            self.suanCalanSarki= self.sarkiListesi[secim - 1]
        else:
            print("Önce şarkı ekleyiniz")
    def sesArttir(self):
        if self.ses <= 90 and self.ses >= 0:
            self.ses +=10 
        else:
            print("Ses daha çok arttırılamaz")
    def sesAzalt(self):
        if self.ses <= 100 and self.ses >= 10:
            self.ses -=10 
        else:
            print("Ses daha çok azaltılamaz")
    def rastgeleSarkiSec(self):
        if len(self.sarkiListesi) > 0:
          global rastgele
          rastgele = int(random.randint(0,len(self.sarkiListesi)))
          self.suanCalanSarki= self.sarkiListesi[rastgele - 1]
          print("Seçilen şarkı numarası:" + str(rastgele))
          print("Şuan Çalan Şarkı:" + self.suanCalanSarki)
        else:
            print("Önce şarkı ekleyiniz")
    def sarkiEkle(self):
        sanatci = input (" Sanatçıyı/Grubu giriniz:")
        sarki = input ("Şarkı İsmini Giriniz: ")
        self.sarkiListesi.append(sanatci +"-"+ sarki)
    def sarkiSil(self):
        sayac = 1
        for sarki in self.sarkiListesi:  
            sayac= 1
            print("{}){}".format(sayac, sarki))
            sayac +=1
        silinecekSarki=int(input("Silinecek şarkının numarasını giriniz : "))
        while silinecekSarki < 1 or silinecekSarki > len(self.sarkiListesi):
           silinecekSarki=int(input("Silinecek şarkının numarasını doğru giriniz : (1-{})".format(len(self.sarkiListesi))))
        self.sarkiListesi.pop(silinecekSarki -1)
    def kapa(self):
        self.durum=False
    def menuGoster(self):
        print(""" 
Şarkı Listesi : {}
Şuan Çalan Şarkı : {}
Ses Düzeyi : {}
1) Şarkı Seç
2) Ses Arttır
3) Ses Azalt
4) Rastgele Şarkı Seç
5) Şarkı Ekle
6) Şarkı Sil
7) Kapat""".format(self.sarkiListesi,self.suanCalanSarki,self.ses))
    def secim(self):
        sec= int(input("Seçiminizi Giriniz:"))
        while sec < 1 or sec > 7 or len(sec)==0 :
           sec= int(input("Seçtiğiniz değer yanlış , lütfen belirtilen aralıklarda değer giriniz (1-7):"))
        return sec
    def calistir(self):
        self.menuGoster()
        secim = self.secim()
        if secim == 1:
            self.sarkiSec()
        if secim == 2:
            self.sesArttir()
        if secim == 3:
            self.sesAzalt()
        if secim == 4:
            self.rastgeleSarkiSec()
        if secim == 5:
            self.sarkiEkle()
        if secim == 6:
            self.sarkiSil()
        if secim == 7:
            self.kapa()

mp3calar= MP3Calar()
while mp3calar.durum:
    mp3calar.calistir()