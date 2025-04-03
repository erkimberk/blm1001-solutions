ogrenciler = []

for i in range(10):
    vize = int(input())
    proje = int(input())
    final = int(input())

    ortalama = (vize * 0.2) + (proje * 0.2) + (final * 0.6)

    ogrenciler.append([vize, proje, final, int(ortalama)])

for ogrenci in ogrenciler:
    for puan in ogrenci:
        print(puan, end=" ")
    print()
