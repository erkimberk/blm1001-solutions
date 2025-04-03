kelime1 = input().lower()
kelime2 = input().lower()
kelime3 = input().lower()

kume1 = set(kelime1)
kume2 = set(kelime2)
kume3 = set(kelime3)

print("1-",sorted(kume1 & kume2 & kume3))

print["2-",sorted(kume1 - {kume2 | kume3})]

print("3-",sorted(kume1 | kume2 | kume3))

print("4-:",kume1 <= kume3)