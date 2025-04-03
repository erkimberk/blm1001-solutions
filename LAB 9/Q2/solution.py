### Kodunuzu bu kismin altina yaziniz.
from abc import ABC, abstractmethod

class Arac(ABC):
    def __init__(self, marka, model, kiralama_ucreti):
        self._marka = marka
        self._model = model
        self.__kiralama_ucreti = kiralama_ucreti

    @abstractmethod
    def bilgi_goster(self):
        pass

    def ucret_arttir(self, miktar):
        if miktar > 0:
            self.__kiralama_ucreti += miktar

    def get_kiralama_ucreti(self):
        return self.__kiralama_ucreti

class Otomobil(Arac):
    def __init__(self, marka, model, kiralama_ucreti, kapasite):
        super().__init__(marka, model, kiralama_ucreti)
        self.__kapasite = kapasite

    def get_kapasite(self):
        return self.__kapasite

    def bilgi_goster(self):
        return f"Otomobil: {self._marka} {self._model}, Kiralama Ücreti: {self.get_kiralama_ucreti()} TL, Kapasite: {self.get_kapasite()} kişi"

class Kamyon(Arac):
    def __init__(self, marka, model, kiralama_ucreti, yuk_kapasitesi):
        super().__init__(marka, model, kiralama_ucreti)
        self.__yuk_kapasitesi = yuk_kapasitesi

    def get_yuk_kapasitesi(self):
        return self.__yuk_kapasitesi

    def bilgi_goster(self):
        return f"Kamyon: {self._marka} {self._model}, Kiralama Ücreti: {self.get_kiralama_ucreti()} TL, Yük Kapasitesi: {self.get_yuk_kapasitesi()} ton"

class Motosiklet(Arac):
    def __init__(self, marka, model, kiralama_ucreti, motor_hacmi):
        super().__init__(marka, model, kiralama_ucreti)
        self.__motor_hacmi = motor_hacmi

    def get_motor_hacmi(self):
        return self.__motor_hacmi

    def bilgi_goster(self):
        return f"Motosiklet: {self._marka} {self._model}, Kiralama Ücreti: {self.get_kiralama_ucreti()} TL, Motor Hacmi: {self.get_motor_hacmi()} cc"

### Kodunuzu bu kismin ustune yaziniz.

## Asagidaki kod degistirilmemelidir.
# Otomobil
o_marka = input()
o_model = input()
o_kira = int(input())
o_kapasite = int(input())

# Kamyon
k_marka = input()
k_model = input()
k_kira = int(input())
k_yuk_kapasitesi = int(input())

# Motosiklet
m_marka = input()
m_model = input()
m_kira = int(input())
m_motor = input()

# Araçların örnekleri oluşturulması ve bilgilerin gösterilmesi
otomobil = Otomobil(o_marka, o_model, o_kira, o_kapasite)
kamyon = Kamyon(k_marka, k_model, k_kira, k_yuk_kapasitesi)
motosiklet = Motosiklet(m_marka, m_model, m_kira, m_motor)

# Bilgilerin gösterilmesi
print(otomobil.bilgi_goster())
print(kamyon.bilgi_goster())
print(motosiklet.bilgi_goster())

# Kira ücret artırımı örneği
otomobil.ucret_arttir(1000)
kamyon.ucret_arttir(-300)
motosiklet.ucret_arttir(200)

# Bilgilerin gösterilmesi
print(otomobil.bilgi_goster())
print(kamyon.bilgi_goster())
print(motosiklet.bilgi_goster())

# Get metodlarına erişim:
print(f"Otomobil kapasitesi:{otomobil.get_kapasite()}")
print(f"Kamyon yuk kapasitesi:{kamyon.get_yuk_kapasitesi()}")
print(f"Motosiklet motor hacmi:{motosiklet.get_motor_hacmi()}")