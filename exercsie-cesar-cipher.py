'''
#1
def kalkulator(a="",b="",c=""):
    if a == "" or b == "" or c == "":
        return ""
    else:
        try:
            a = float(a)
            b = float(b)
            if c == "*":
                return a*b
            elif c == "/":
                if b == 0:
                    return "nol"
                else:
                    return a/b
            elif c == "+":
                return a+b
            elif c == "-":
                return a-b
            else:
                return "Operator yang anda masukkan salah, hanya bisa * / + -"
        except:
            return "angka"

input1 = input("Masukkan angka 1  : ")
input2 = input("Masukkan angka 2  : ")
input3 = input("Masukkan Operator : ")
hasil = kalkulator(input1,input2,input3)
if hasil == "angka":
    print("Angka yang anda masukkan salah")
elif hasil == "nol":
    print("Tidak bisa membagi dengan angka 0")
elif kalkulator(input1,input2,input3) != "":
    print("Hasil dari {} {} {} adalah {}".format(input1,input3,input2,hasil))
else:
    print("Anda belum memasukkan angka 1, angka 2, atau operator")
'''

#2
huruf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
c = ""
def cesar(kata="",angka=""):
    if kata == "" or angka == "":
        print("Anda belum memasukkan kata atau angka")
    else:
        if kata.lower().isalpha():
            try:
                if int(angka) > 0:
                    angka = int(angka)%26
                    b = 0
                    c = ""
                    for a in kata.lower():
                        if huruf.index(a)+angka > 25:
                            b = huruf.index(a)+angka - 26
                        else:
                            b = huruf.index(a)+angka
                        c = c + huruf[b]
                elif int(angka) < 0:
                    angka = abs(int(angka))%26
                    b = 0
                    c = ""
                    for a in kata.lower():
                        if huruf.index(a)-angka < 0:
                            b = huruf.index(a)-angka + 26
                        else:
                            b = huruf.index(a)-angka
                        c = c + huruf[b]         
                print(f"Hasil Caesar Cipher : {c}")
            except:
                print("Hanya menerima angka bulat")
        else:
            print("Kata yang anda masukkan salah")

x = input("Masukkan kata  : ")
y = input("Masukkan angka : ")
cesar(x,y)