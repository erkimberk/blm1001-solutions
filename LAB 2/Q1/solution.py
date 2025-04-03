import math

def cevre_alan_hesapla(yaricap):
    cevre = 2 * math.pi * yaricap
    alan = math.pi * (yaricap ** 2)
    return cevre,alan

sayi1 = abs(int(input()))
sayi2 = abs(int(input()))

baslangic = min(sayi1,sayi2)
bitis = max(sayi1,sayi2)

for yaricap in range(baslangic,bitis,3):
    cevre,alan = cevre_alan_hesapla(yaricap)
    print(f"{yaricap:<10}{cevre:<10.2f}{alan:<10.2f}")

