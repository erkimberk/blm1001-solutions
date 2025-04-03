toplam = 0

while True:
    sayi = int(input())

    if (sayi == 0):
        break

    if (sayi % 9 == 0):
        toplam += sayi

print(toplam)