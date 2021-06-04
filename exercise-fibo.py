
#1
from functools import reduce

def fibonacci(num):
    fibo = []
    if num == 1:
        fibo.extend([0,1])
    elif num == 2:
        fibo.extend([0,1,1])
    else:
        fibo.extend([0,1,1])
        for a in range (3,num+1):
            fibo.append(fibo[a-1]+fibo[a-2])
    return " ".join(map(str,fibo)), reduce(lambda x,y:x+y,fibo)

try:
    input1 = int(input("Masukkan angka : "))
    if input1 > 0:
        deret, jumlah = fibonacci(input1)
        print("{} deret angka pertama baris fibonacci adalah {} dan jumlahnya {}".format(input1,deret,jumlah))
    else:
        print("Tidak menerima angka negatif")
except:
    print("Angka yang anda masukkan salah")

'''
#2
from functools import reduce
angka = [10,7,9,1,7,120,4,6,8,10,8,1,1,105,6,6,1,6,10,4,1,8,3,9,9,6,6,3,100,1,5,9,10,6,1,1,9,9,9,5,2,8,10,8,9,5,9,9,2,3,2,10,4,10,
        5,2,4,7,3,9,6,1,8,4,3,6,4,5,4,8,2,4,2,6,3,9,6,5,9,6,4,6,1,3,6,8,6,2,9,6,3,8,3,8,2,1,5,8,8,6]

def mean(num):
    return reduce(lambda x,y:x+y,num)/len(num)

def median(num):
    if len(num)%2 != 0:
        return num[int(len(num)/2+1)]
    else:
        return (num[int((len(num)/2))] + num[int(len(num)/2+1)]) / 2

def modus(num):
    hitung = dict()
    hasil = []
    for a in num:
        hitung[a] = num.count(a)
    hasil = list(hitung.values())
    hasil = ngurutin(hasil)
    for a,b in hitung.items():
        if b == hasil[len(hasil)-1]:
            return a

def q1(num):
    lowhalf = num[:int(len(num)/2)]
    return median(lowhalf)

def q3(num):
    if len(num)%2 != 0:
        highhalf = num[int(len(num)/2+2):]
    else:
        highhalf = num[int(len(num)/2+1):]
    return median(highhalf)
 
def outlier(num):
    out = [a for a in num if (a<(q1(num)-1.5*(q3(num)-q1(num))) or a>(q3(num)+1.5*(q3(num)-q1(num))))]
    return out

def ngurutin(num):
    for a in range(len(num)):
        for b in range(len(num)-1):
            if num[b] > num[b+1]:
                temp = num[b+1]
                num[b+1] = num[b]
                num[b] = temp
    return num

angka = ngurutin(angka)
print("Nilai mean dari baris angka adalah " + str(mean(angka)))
print("Nilai median dari baris angka adalah " + str(median(angka)))
print("Nilai modus dari baris angka adalah " + str(modus(angka)))
print("Nilai quartile 1 dari baris angka adalah " + str(q1(angka)))
print("Nilai quartile 3 dari baris angka adalah " + str(q3(angka)))
if len(outlier(angka)) > 0:
    print("Nilai outlier dari baris angka adalah " + " ".join(map(str, outlier(angka))))
else:
    print("Baris angka tidak memiliki outlier")


#3
def urutnaik(num):
    for a in range(len(num)):
        for b in range(len(num)-1):
            if num[b] > num[b+1]:
                temp = num[b+1]
                num[b+1] = num[b]
                num[b] = temp
    return num

def urutturun(num):
    for a in range(len(num)):
        for b in range(len(num)-1):
            if num[b] < num[b+1]:
                temp = num[b+1]
                num[b+1] = num[b]
                num[b] = temp
    return num

def minmax(num):
    deret = urutnaik(num)
    return deret[0], deret[len(deret)-1]

w = 1
while (w < 11):
    try:
        list1 = []
        input1 = input("Masukkan angka {}: ".format(w))
        list1.append(int(input1))
        w+=1
    except:
        print("Angka yang anda masukkan salah")
# list1 = [100,1,5,9,10,6,1,1,9,9]

loop = True
while loop:
    print("Menu Utama")
    print("1. Ascending\n2. Descending\n3. Min & Max\n4. Exit")
    pilihan = input("Masukkan pilihan : ")
    if pilihan == "1":
        baru = urutnaik(list1)
        print("Urutan angka dari yang paling kecil adalah " + " ".join(map(str,baru)))
        print("")
    elif pilihan == "2":
        baru = urutturun(list1)
        print("Urutan angka dari yang paling besar adalah " + " ".join(map(str,baru)))
        print("")
    elif pilihan == "3":
        baru1, baru2 = minmax(list1)
        print("Angka minimum adalah {} dan angka maksimum adalah {}".format(baru1,baru2))
        print("")
    elif pilihan == "4":
        loop = False
    else:
        print("Pilihan yang anda masukkan salah")
'''
