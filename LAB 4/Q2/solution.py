def myfunction(hucre_degerleri_listesi, baslangic_hucresi_numarasi, bitis_hucresi_numarasi, aranan_deger):
    for hucre_numarasi in range(baslangic_hucresi_numarasi, bitis_hucresi_numarasi + 1):
        if (hucre_degerleri_listesi[hucre_numarasi] == aranan_deger):
            print(hucre_numarasi)
            return ""

    print("False")


hucre_degerleri_listesi = []

for i in range(32):
    hucre_degeri = int(input())
    hucre_degerleri_listesi.append(hucre_degeri)

baslangic_hucresi_numarasi = int(input())
bitis_hucresi_numarasi = int(input())
aranan_deger = int(input())

myfunction(hucre_degerleri_listesi, baslangic_hucresi_numarasi, bitis_hucresi_numarasi, aranan_deger)