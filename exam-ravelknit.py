#Soal 3
def ravel(kata):
    c = ""
    for a in range(len(kata)+1):
        for b in range(0,a):
            c += kata[b]
    return c

panjang = []
jumlah = 0
for a in range(20):
    jumlah += a
    panjang.append(jumlah)

# print(panjang)

def knit(kata):
    for a in panjang:
        if len(kata) == a:
            return kata[len(kata)-panjang.index(a):]

print(ravel("Purwadhika"))
print(ravel("Digital"))
print(ravel("Coding"))
print(ravel("School"))

print(knit("PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika"))
print(knit("DDiDigDigiDigitDigitaDigital"))
print(knit("CCoCodCodiCodinCoding"))
print(knit("SScSchSchoSchooSchool"))