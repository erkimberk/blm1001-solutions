import math

def kok_log_hesapla(sayi):
    kok = math.sqrt(sayi)
    logaritma = math.log10(sayi)
    return kok,logaritma

sayi1 = abs(int(input()))
sayi2 = abs(int(input()))

baslangic = min(sayi1,sayi2)
bitis = max(sayi1,sayi2)

for sayi in range(baslangic,bitis+1):
    if (sayi % 2 != 0):
        kok,logaritma = kok_log_hesapla(sayi)
        print(f"{sayi:<10}{kok:<10.2f}{logaritma:<10.2f}")