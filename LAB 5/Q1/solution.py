atletler = []

for atlet in range(8):
    atlet = []

    for sure in range(3):
        sure = int(input())
        atlet.append(sure)

    ortalama = sum(atlet) // len(atlet)

    atletler.append(atlet + [ortalama])

for atlet in atletler:
    for sure in atlet:
        print(sure, end=" ")
    print()
