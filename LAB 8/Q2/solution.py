import re

metin = input()

eposta_regex = r"[a-zA-Z._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}"

epostalar = re.findall(eposta_regex, metin)

for eposta in epostalar:
    print(eposta)

yeni_metin = re.sub(eposta_regex, "[E-POSTA GIZLI]", metin)

print(yeni_metin)