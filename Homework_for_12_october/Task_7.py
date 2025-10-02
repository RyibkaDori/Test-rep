import string
B = []
Slovnik = {}
with open("Text.txt", "r", encoding="utf-8") as f:
    text = f.read()
lower_text = text.lower()
lower_text_without = [symb for symb in lower_text if symb not in string.punctuation and symb !='—']
a = ''.join(lower_text_without)
hz = a.split()
for i in hz:
    B.append(hz.count(i))
Slovar = {slovo: chast for slovo, chast in zip(hz, B)}
d = len(Slovar)
print(Slovar)
z =list(Slovar.keys())
s = list(Slovar.values())
qw = 0
e =0
a=max(s)
while e < 10:
    for key in z:
        if (Slovar[key] == a):
            print(key, Slovar[key])
            e=e+1
            s.remove(Slovar[key])
            z.remove(key)
            a=max(s)
            break


