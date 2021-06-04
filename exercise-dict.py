'''
#1
data = {
    "senin" : "monday",
    "selasa" : "tuesday",
    "rabu" : "wednesday",
    "kamis" : "thursday",
    "jumat" : "friday",
    "sabtu" : "saturday",
    "minggu" : "sunday"
}

while True:
    hari = input("Masukkan nama hari : ")
    if hari == 'exit':
        break
    elif hari.isalpha():
        if hari.lower() in data.values():
            for a, b in data.items():
                if b == hari.lower():
                    print("The day that you choose is {} and in bahasa is {}".format(hari.capitalize(),a.capitalize()))
                    break
        elif hari.lower() in data.keys():
            print("Hari yang anda pilih adalah {} dan dalam bahasa inggris adalah {}".format(hari.capitalize(),data[hari].capitalize()))
        else:
            print("Hari yang anda masukkan salah")
    else:
        print("Tidak menerima selain alfabet")
'''
#2
kodemorse = {
  "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
  "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", 
  "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
  ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"
}
tukar =""
kata2 = input("Masukkan kata : ")
kata = kata2.lower()
if "|" in kata:
    gagal = False
    kode = kata.split("|")
    if '' in kode:
        kode.remove('')
    for a in kode:
        if a in kodemorse.values():
            for i, j in kodemorse.items():
                if j == a:
                    tukar += str(i)
        else:
            print("Kode yang anda masukkan salah")
            break
    else:
        print("Kode morse yang anda masukkan {} jika diubah menjadi kata-kata menjadi {}".format(kata2,tukar))
else:
    gagal = False
    try:
        fl = float(kata)
        if fl.is_integer():
            katasplit = kata.split()
            for a in katasplit:
                for b in a:
                    if b not in kodemorse.keys():
                        print("Tidak bisa dikonversi ke kode morse")
                        gagal = True
                        break
                    else:
                        tukar += kodemorse.get(b) + '|'
            else:
                if not gagal:
                    print("Kata yang anda masukkan adalah {} jika diubah menjadi kode morse menjadi {}".format(kata2, tukar))
        else:
            print("Tidak menerima angka pecahan")
    except:
        katasplit = kata.split()
        for a in katasplit:
            for b in a:
                if b not in kodemorse.keys():
                    print("Tidak bisa dikonversi ke kode morse")
                    gagal = True
                    break
                else:
                    tukar += kodemorse.get(b) + '|'
        else:
            if not gagal:
                print("Kata yang anda masukkan adalah {} jika diubah menjadi kode morse menjadi {}".format(kata2, tukar))
'''
#3
A = list()
B = list()
C = list()
D = list()
E = list()

for a in range (1,101,1):
    if a % 2 == 0:
        A.append(a)
# print(A)

for b in range (1,101,1):
    if b % 2 == 1:
        B.append(b)
# print(B)

for c in range (-100,0,1):
    C.append(c)
# print(C)

for d in range (2,101,1):
    for d1 in range (2,d,1):
        if d % d1 == 0:
            break
    else:
        D.append(d)
print(D)

for e in range (1,101,1):
    for e1 in range (1,e,1):
        if e1 != 1:
            if e % e1 == 0:
                E.append(e)
                break
            else:
                continue
        elif e1 == 1 and e1 not in E:
            E.append(e1)
# print(E)

set1 = set(A)
set2 = set(B)
set3 = set(C)
set4 = set(D)
set5 = set(E) 
print("\na. A u B u C u D u E")
print("Hasil = {}".format(set1 | set2 | set3 | set4 | set5), end='\n')
print("-"*200)
print("\nb. (A n B) u (D n E)")
print("Hasil = {}".format((set1 & set2) | (set4 & set5)), end='\n')
print("-"*200)
print("\nc. (A u B) n (D u E)")
print("Hasil = {}".format((set1 | set2) & (set4 | set5)), end='\n')
print("-"*200)
print("\nd. (A u B) - (D u E)")
print("Hasil = {}".format((set1 | set2) - (set4 | set5)), end='\n')
print("-"*200)
print("\ne. (A u B u C) - (A n E)")
print("Hasil = {}".format((set1 | set2 | set3) - (set1 & set5)), end='\n')
'''