import re

metin = input()

telefon_regex = r"0\(\d{3}\) \d{3}-\d{4}"

telefonlar = re.findall(telefon_regex,metin)

for telefon in telefonlar:
    print(telefon)

yeni_metin = re.sub(telefon_regex,"[TELEFON GİZLİ]",metin)

print(yeni_metin)