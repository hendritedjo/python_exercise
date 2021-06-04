'''
arabroma = {}
global sisa
global rome
global angka
sisa = 0
rome = ""

def konv_ratus():
    global angka
    global sisa
    global rome
    rome = ""
    if sisa >= 900:
        rome += "CM"
        sisa -= 900
    elif sisa >= 500:
        rome += "D"
        sisa -= 500
    elif sisa >= 400:
        rome += "CD"
        sisa -= 400
    angka = sisa//100
    sisa = sisa%100
    for a in range (1,angka+1,1):
        rome += "C"
    return rome

def konv_puluhan():
    global angka
    global sisa
    global rome
    rome = ""
    if sisa >= 90:
        rome+= "XC"
        sisa -= 90
    elif sisa >= 50:
        rome += "L"
        sisa -= 50
    elif sisa >= 40:
        rome += "XL"
        sisa -= 40
    angka = sisa//10
    sisa = sisa%10
    for a in range (1,angka+1,1):
        rome += "X"
    return rome

def konv_satuan(num):
    satu = {1: "I", 2: "II", 3 : "III", 4 : "IV", 5 : "V", 6 : "VI", 7 : "VII", 8 : "VIII", 9 : "IX"}
    global angka
    global sisa
    global rome
    rome = ""
    if sisa >= 9:
        rome+= "IX"
        sisa -= 9
    elif sisa >= 5:
        rome += "V"
        sisa -= 5
    elif sisa >= 4:
        rome += "IV"
        sisa -= 4
    for a in range (1,sisa+1,1):
        rome += "I"    
    return rome

angka = input("Masukkan angka : ")
angka = int(angka)
hasil = ""
if angka >= 1000:
    sisa = angka%1000
    angka = angka//1000
    for a in range (1,angka+1,1):
        rome += "M"
    hasil = rome + konv_ratus() + konv_puluhan() + konv_satuan()
elif angka >=100:
    sisa = angka%1000
    angka = angka//1000
    hasil = konv_ratus() + konv_puluhan() + konv_satuan()
elif angka >=10:
    sisa = angka%100
    angka = angka//100
    hasil = konv_puluhan() + konv_satuan()
else:
    sisa = angka
    hasil = konv_satuan()
    
    
    

print(hasil)

'''
satu = {0 : "", 1: "I", 2: "II", 3 : "III", 4 : "IV", 5 : "V", 6 : "VI", 7 : "VII", 8 : "VIII", 9 : "IX"}
puluh = {0 : "", 1: "X", 2: "XX", 3 : "XXX", 4 : "XL", 5 : "L", 6 : "LX", 7 : "LXX", 8 : "LXXX", 9 : "XC"}
ratus = {0 : "", 1: "C", 2: "CC", 3 : "CCC", 4 : "CD", 5 : "D", 6 : "DC", 7 : "DCC", 8 : "DCCC", 9 : "CM"}
ribu = {0 : "", 1: "M", 2: "MM", 3 : "MMM", 4 : "MV"}
romainvalid = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                "A", "B", "E", "F", "G", "H", "J", "K", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "Y", "Z"]
romaunik = {"IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900, "MV" : 4000, "MX" : 9000}
romabiasa = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
urutanroma = {"I" : ["L", "C", "D", "M"], "V" : ["X", "L", "C", "D", "M"], "X" : ["D", "M"], "L" : ["C", "D", "M"], "C" : ["M"], "D" : ["M"], "M" : [""]}
roma1 = ["V", "L", "D"]
roma2 = {"I" : ["V", "X", "L", "C", "D", "M"], "X" : ["L", "C", "D", "M"], "C" : ["D", "M"], "M" : [""]}

def konv_arabroma(kamus, num):
    for a in kamus.keys():
        if a == num:
            return kamus[a]

def konv_romaarab(unik, biasa, huruf):
    arab = 0
    hurufrep = huruf
    for a in huruf: # cek urutan angka romawi
        if a in roma1 and huruf.count(a) > 1:
            return "Angka romawi yang anda masukkan salah"
        elif a in roma2.keys() and huruf.count(a) > 3:
            return "Angka romawi yang anda masukkan salah"
        elif a in roma2.keys() and huruf.count(a) > 1:
            temp = huruf[huruf.index(a)+1:]
            for b in temp:
                if b in roma2[a]:
                    return "Urutan angka romawi salah"
        for b in hurufrep:
            if b in urutanroma[a]:
                return "Urutan angka romawi salah" 
        hurufrep = hurufrep.replace(a,"")
    for a in range(len(huruf)):
        for b in unik.keys():
            if b in huruf:
                huruf = huruf.replace(b,"",1)
                arab += unik[b]
    else:
        for a in range(len(huruf)):
            for b in biasa.keys():
                if b in huruf:
                    huruf = huruf.replace(b,"",1)
                    arab += biasa[b]
    return arab


angka = input("Masukkan angka : ")
if angka.isdigit():
    if int(angka) < 1:
        print("Angka minimum 1")
    elif int(angka) < 10:
        print(konv_arabroma(satu,int(angka)))
    elif int(angka) < 100:
        print(konv_arabroma(puluh,int(angka[0])),end="")
        print(konv_arabroma(satu,int(angka[1])))
    elif int(angka) < 1000:
        print(konv_arabroma(ratus,int(angka[0])),end="")
        print(konv_arabroma(puluh,int(angka[1])),end="")
        print(konv_arabroma(satu,int(angka[0])))
    elif int(angka) < 4000:
        print(konv_arabroma(ribu,int(angka[0])),end="")
        print(konv_arabroma(ratus,int(angka[1])),end="")
        print(konv_arabroma(puluh,int(angka[2])),end="")
        print(konv_arabroma(satu,int(angka[3])))
    else:
        print("Angka maksimum 4000")
elif angka.isalpha():
    for a in angka:
        if a in romainvalid:
            print("Angka yang anda masukkan salah")
            break
    else:
        print(konv_romaarab(romaunik,romabiasa,angka))
else:
    print("Angka yang anda masukkan salah")


