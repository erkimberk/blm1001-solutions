def print_soccer_table(takimlar,sampiyonluk_sayilari):
    print(f"{'Takim Adi':<20} {'Sampiyonluk Sayisi':<20} {'Yildizlar':<20}")

    for index in range(len(takimlar)):
        yildiz_sayisi = sampiyonluk_sayilari[index] // 7
        yildiz_stringi = yildiz_sayisi * "*"

        print(f"{takimlar[index]:<20} {sampiyonluk_sayilari[index]:<20} {yildiz_stringi:<20}")

takimlar = list()
sampiyonluk_sayilari = []
counter = int(input())

for i in range(counter):
    takim = input()
    takimlar.append(takim)

    sampiyonluk_sayisi = int(input())
    sampiyonluk_sayilari.append(sampiyonluk_sayisi)

print_soccer_table(takimlar,sampiyonluk_sayilari)