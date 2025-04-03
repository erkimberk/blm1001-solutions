def min_max_ziyaretci_bul(ziyaretci_listesi,baslangic_saati,bitis_saati):
    for saat in range(baslangic_saati,bitis_saati+1):
        if (saat == baslangic_saati):
            minimum_ziyaretci_indexi = saat
            maksimum_ziyaretci_indexi = saat

        if (ziyaretci_listesi[saat] < ziyaretci_listesi[minimum_ziyaretci_indexi]):
            minimum_ziyaretci_indexi = saat

        if (ziyaretci_listesi[saat] > ziyaretci_listesi[maksimum_ziyaretci_indexi]):
            maksimum_ziyaretci_indexi = saat

    print("{}:00".format(maksimum_ziyaretci_indexi))
    print(f"{minimum_ziyaretci_indexi}:00")

ziyaretci_sayilari = []

for i in range(24):
    ziyaretci_sayisi = int(input())
    ziyaretci_sayilari.append(ziyaretci_sayisi)


baslangic_saati = int(input())
bitis_saati = int(input())

min_max_ziyaretci_bul(ziyaretci_sayilari,baslangic_saati,bitis_saati)