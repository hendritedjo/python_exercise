# Tugas 1

try:
    temp = int(input('Masukkan jumlah hari (1 - 4000) : '))
    if (temp > 4000):
        print('Jumlah hari melebihi batas')
    elif (temp < 0):
        print('Jumlah hari di bawah batas')
    else:
        tahun = int(temp/365)
        bulan = int((temp%365)/30)
        minggu = int(((temp%365)%30)/7)
        hari = int((((temp%365)%30)%7))
        print('{:02d} tahun {:02d} bulan {:02d} minggu {:02d} hari'.format(tahun,bulan,minggu,hari))
except:
    print('Jumlah hari tidak bisa menerima string atau angka desimal')



# Tugas 2
'''
try:
    error2 = 2
    tampung1 = input('Masukkan tinggi badan anda : ')
    tampung2 = input('Masukkan berat badan anda : ')
    tinggi = int(tampung1)
    berat = int(tampung2)
    if ((tinggi < 0) or (berat < 0)):
        error2 = 1
        tinggi /= 0
    elif ((tinggi > 300) or (berat > 250)):
        error2 = 3
        tinggi /= 0
    else:
        BMI = round( (berat / ((tinggi*tinggi) / 10000)), 2)
        if (BMI<18.5):
            cat = 'berat badan kurang'
        elif (BMI<24.9):
            cat = 'berat badan ideal'
        elif (BMI<29.9):
            cat = 'berat badan berlebih'
        elif (BMI<39.9):
            cat = 'berat badan sangat berlebih'
        else:
            cat = 'obesitas'
        print('Tinggi badan anda {} meter dan berat anda {} kg, BMI anda {} dan anda termasuk {}'.format(tinggi/100, berat, BMI,cat))
except:
    if (error2 == 1):
        print('Tidak menerima angka negatif')
    elif (error2 == 2):
        print('Angka yang anda masukkan salah')
    elif (error2 == 3):
        print('Tinggi / berat badan anda di atas batas')
    else:
        print('Ada error yang tidak diketahui')


# Tugas 3

try:
    error3 = 3
    nilai = float(input('Masukkan nilai: '))
    if (nilai > 100):
        error3 = 1
        nilai /= 0
    elif (nilai < 0):
        error3 = 2
        nilai /= 0
    else:
        if (nilai >= 90):
            kategori = 'Grade A'
        elif (nilai >= 85):
            kategori = 'Grade A-'
        elif (nilai >= 80):
            kategori = 'Grade B'
        elif (nilai >= 75):
            kategori = 'Grade B-'
        elif (nilai >= 70):
            kategori = 'Grade C'
        elif (nilai >= 65):
            kategori = 'Grade D'
        elif (nilai >= 40):
            kategori = 'Perlu REMEDIAL'
        else:
            kategori = 'TIDAK LULUS'
        print('Nilai anda {} dan anda {}'.format(nilai,kategori))

except:
    if (error3 == 1):
        print('Nilai di luar jangkauan')
    elif (error3 == 2):
        print('Tidak menerima angka negatif')
    elif (error3 == 3):
        print('Angka yang anda masukkan salah')
    else:
        print('Ada error yang tidak diketahui')
'''
