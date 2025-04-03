basarili_ögrenci_sayisi = 0
basarisiz_ögrenci_sayisi = 0

for i in range(10):
    alinan_not = int(input())

    if (60 <= alinan_not <= 100):
        basarili_ögrenci_sayisi += 1

    elif (0 <= alinan_not <= 59):
        basarisiz_ögrenci_sayisi += 1

print(basarili_ögrenci_sayisi)
print(basarisiz_ögrenci_sayisi)