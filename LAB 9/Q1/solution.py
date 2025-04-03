### Kadunuzu bu kismin altina yaziniz.
from abc import ABC, abstractmethod

class Calisan(ABC):
    def __init__(self, ad, soyad, maas):
        self._ad = ad
        self._soyad = soyad
        self.__maas = maas

    @abstractmethod
    def bilgi_goster(self):
        pass

    def maas_arttir(self, miktar):
        if miktar > 0:
            self.__maas += miktar

    def get_maas(self):
        return self.__maas

class OgretimUyesi(Calisan):
    def __init__(self, ad, soyad, maas, ders_sayisi):
        super().__init__(ad, soyad, maas)
        self.__ders_sayisi = ders_sayisi

    def get_ders_sayisi(self):
        return self.__ders_sayisi

    def bilgi_goster(self):
        return f"Ogretim Uyesi: {self._ad} {self._soyad}\nMaas: {self.get_maas()} TL\nDers Sayisi: {self.get_ders_sayisi()}"

class ArastirmaGorevlisi(Calisan):
    def __init__(self, ad, soyad, maas, proje_sayisi):
        super().__init__(ad, soyad, maas)
        self.__proje_sayisi = proje_sayisi

    def get_proje_sayisi(self):
        return self.__proje_sayisi

    def bilgi_goster(self):
        return f'Arastirma Gorevlisi: {self._ad} {self._soyad}\nMaas: {self.get_maas()} TL\nProje_sayisi: {self.get_proje_sayisi()}'

class IdariCalisan(Calisan):
    def __init__(self, ad, soyad, maas, gorev):
        super().__init__(ad, soyad, maas)
        self.__gorev = gorev

    def get_gorev(self):
        return self.__gorev

    def bilgi_goster(self):
        return f'Idari Calisan: {self._ad} {self._soyad}\nMaas: {self.get_maas()} TL\nGorev: {self.get_gorev()}'




### Kadunuzu bu kismin ustune yaziniz.

## Asagidaki kod degistirilmemelidir.
# Ogretim uyesi
ou_ad = input()
ou_soyad = input()
ou_maas = int(input())
ou_ders_sayisi = int(input())

# Arastirma gorevlisi
ag_ad = input()
ag_soyad = input()
ag_maas = int(input())
ag_proje_sayisi = int(input())

# Idari calisan
ic_ad = input()
ic_soyad = input()
ic_maas = int(input())
ic_gorev = input()

# Calisan ornekleri oluşturulması ve bilgilerin gösterilmesi
ogretim_uyesi = OgretimUyesi(ou_ad, ou_soyad, ou_maas, ou_ders_sayisi)
arastirma_gorevlisi = ArastirmaGorevlisi(ag_ad, ag_soyad, ag_maas, ag_proje_sayisi)
idari_calisan = IdariCalisan(ic_ad, ic_soyad, ic_maas, ic_gorev)

print(ogretim_uyesi.bilgi_goster())
print(arastirma_gorevlisi.bilgi_goster())
print(idari_calisan.bilgi_goster())

# Maas artırımı örneği
ogretim_uyesi.maas_arttir(1000)
arastirma_gorevlisi.maas_arttir(-300)

# Bilgilerin gösterilmesi
print(ogretim_uyesi.bilgi_goster())
print(arastirma_gorevlisi.bilgi_goster())
print(idari_calisan.bilgi_goster())

# Get metodlarına erişim:
print(f"Ogretim uyesi ders sayisi:{ogretim_uyesi.get_ders_sayisi()}")
print(f"Arastirma gorevlisi proje sayisi:{arastirma_gorevlisi.get_proje_sayisi()}")
print(f"Idari calisan gorev:{idari_calisan.get_gorev()}")