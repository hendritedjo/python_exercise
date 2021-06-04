
#1
hari = ['senin','selasa','rabu','kamis','jumat','sabtu','minggu']
try:
    inputhari = input("Masukkan hari : ")
    inputangka = int(input("Masukkan jumlah : "))
    inputhari = inputhari.lower()
    if (inputhari not in hari):
        print("Nama hari yang anda masukkan salah")
    else:
        sisa = inputangka % 7
        if (hari.index(inputhari)+sisa) > 6:
            sisa = sisa + hari.index(inputhari) - 7
        elif (hari.index(inputhari)+sisa < 0):
            sisa = sisa + hari.index(inputhari) + 7
        print("Hari ini hari {}. {} hari lagi adalah hari {}".format(inputhari.capitalize(),str(inputangka),hari[sisa].capitalize()))
except:
    print("Jumlah yang anda masukkan salah")
'''
#2
kalimat = input("Masukkan kalimat : ")
for a in kalimat:
    if a in ["0","1","2","3","4","5","6","7","8","9"]:
        print("Tidak menerima angka")
        break
else:
    kalimat = kalimat.split()
    if kalimat.isalpha():
        for a in kalimat:
            print(a[::-1], end=" ")
            print("")
    else:

#3
kata1 = input("Masukkan kata : ")
for a in kata1:
    if a in ["0","1","2","3","4","5","6","7","8","9"]:
        print("Tidak menerima angka")
        break
else:
    if kata1.isalpha():
        kata2 = kata1[::-1]
        if kata1.lower() == kata2.lower():
            print("Kata tersebut {} merupakan Palindrome".format(kata1))
        else:
            print("Kata tersebut {} bukan merupakan Palindrome".format(kata1))
    else:
        print("Tidak menerima di luar alphabet")
'''