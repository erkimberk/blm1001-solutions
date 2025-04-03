def print_table(calisanlar,proje_sayilari):
    print(f"{'Calisan Adi':<20} {'Proje Sayisi':<20} {'Oduller':<20}")

    for index in range(len(calisanlar)):
        odul_sayisi = proje_sayilari[index] // 5
        odul_sayisi_stringi = odul_sayisi * "+"

        print(f"{calisanlar[index]:<20} {proje_sayilari[index]:<20} {odul_sayisi_stringi:<20}")

calisanlar = list()
proje_sayilari = []

counter = int(input())

for i in range(counter):
    calisan = input()
    calisanlar.append(calisan)

    proje_sayisi = int(input())
    proje_sayilari.append(proje_sayisi)

print_table(calisanlar,proje_sayilari)