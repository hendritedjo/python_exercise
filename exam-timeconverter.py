#Soal 1
def timeConverter(seconds):
    jam = seconds // 3600
    menit = seconds % 3600 // 60
    detik = (seconds % 3600) % 60
    return jam, menit, detik

try:
    input1 = int(input("Masukkan detik : "))
    if input1 > 359999 or input1 < 0:
        print("Invalid input")
    else:
        a = timeConverter(input1)
        print("Konversi {:02d}:{:02d}:{:02d}".format(a[0], a[1], a[2]))
except:
    print("Invalid input")