sozluk = {}

eklenecek_kelime_sayisi = int(input())

for i in range(eklenecek_kelime_sayisi):
    key, value = input().split()
    sozluk[key] = value

islem = int(input())

while (islem != -1):

    if (islem == 0):
        kelime = input()

        if (kelime in sozluk):
            print(f"{sozluk[kelime]}")
        else:
            print(f"{kelime} bulunamadi!")

    elif (islem == 1):
        key, value = input().split()
        sozluk[key] = value

    elif (islem == 2):
        for key, value in sorted(sozluk.items()):
            print(f"{key}: {value}")

    islem = int(input())