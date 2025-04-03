sozluk = {}

toplam_sehir_sayisi = int(input())

for i in range(toplam_sehir_sayisi):
    key, value = input().split()
    sozluk[key] = value

islem = int(input())

while (islem != -1):

    if (islem == 0):
        sehir = input()
        if(sehir in sozluk):
            print(f"{sozluk[sehir]}")

        else:
            print(f"{sehir} bulunamadi!")

    if (islem == 1):
        key, value = input().split()
        sozluk[key] = value

    if(islem == 2):
        for sehir_adi, plaka in sorted(sozluk.items()):
            print(f"{sehir_adi}: {plaka}")

    islem = int(input())