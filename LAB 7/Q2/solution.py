print("8 ogrencinin isimlerini giriniz:")
ogrenciler = [input() for i in range(8)]

resim = [int(input()) for i in range(4)]
muzik = [int(input()) for i in range(4)]
tiyatro = [int(input()) for i in range(4)]

resim_kulubu = {ogrenciler[index] for index in resim}
muzik_kulubu = {ogrenciler[index] for index in muzik}
tiyatro_kulubu = {ogrenciler[index] for index in tiyatro}

tum_kulupler = resim_kulubu & muzik_kulubu & tiyatro_kulubu

print("1-",resim_kulubu.isdisjoint(tiyatro_kulubu))

print("2-",sorted(resim_kulubu ^ muzik_kulubu))

print("3-",sorted(tum_kulupler))

ogrenciler_kumesi = set(ogrenciler)
butun_kulupler_birlesimi = resim_kulubu | muzik_kulubu | tiyatro_kulubu

print("4-",sorted(ogrenciler_kumesi - butun_kulupler_birlesimi))