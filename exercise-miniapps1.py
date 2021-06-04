alattulis = ['kertas', 'buku', 'pulpen', 'pena',
             'pensil', 'penghapus', 'tipex', 'penggaris', 'spidol']
data = ['pensil', 'pulpen', 'penghapus', 'penggaris', 'pulpen']
utama = True
loop = True
password = 'purwadhika'
# login = ''

coba = 1
# batas = 6

while coba <= 6:
    login = input("Masukkan password Anda : ")
    if login != password and coba == 6:
        print("Password Anda salah, kesempatan Anda habis")
        break
    elif login != password:
        print("Password yang Anda masukkan salah, silahkan coba lagi")
    else:
        print("Password Anda benar, Anda berhasil login")
        coba = 7
    coba += 1
else:
# menu_utama = ['1. Cetak Isi daftar Barang', '2. Menambah Data Barang', '3. Mengubah Data Barang', '4. Menghapus Data Barang', '5. Keluar Aplikasi']
    while (utama):
        print("\n"
            "-----Nama Aplikasi-----\n"
            "1. Cetak Isi daftar Barang\n"
            "2. Menambah Data Barang\n"
            "3. Mengubah Data Barang\n"
            "4. Menghapus Data Barang\n"
            "5. Keluar Aplikasi\n"
            "-----------------------")
        try:
            perintah = int(input("Masukkan pilihan menu : "))
            if perintah == 1:  # menu cetak
                print("Data Alat Tulis : ")
                if data == []:
                    print("Daftar Alat Tulis Masih Kosong")
                for d in data:
                    print(d)
                print("\n"
                    "-----Mini Menu-----\n"
                    "1. kembali ke menu awal\n"
                    "-----------------------")
                while True:
                    try:
                        pilihan = int(input("Tentukan pilihanmu sekarang : "))
                        b = ""
                        if pilihan == 1:
                            b = 'menu awal'
                            break
                        else:
                            print("cuma 1 aja bossss. g ade yang lain")
                            continue
                    except:
                        print("cuma 1 aja bossss. g ade yang lain")
                        continue
#================================================================================================================================================================================
            elif perintah == 2:  # menu tambah
                while loop:
                    print("\n------MENAMBAH DATA------\n")
                    tambah = input("Masukkan data yang akan ditambahkan : ")            #input barang yang akan ditambahkan
                    tambah = tambah.lower()                                             #input diseragamkan di lower case
                    if tambah in alattulis and tambah not in data:                      #apabila barang yang akan ditambahkan ada dalam alattulis dan belum ada di data
                        data.append(tambah)                                             #tambahkan ke data
                    elif tambah in alattulis and tambah in data:                        #apabila ada di dalam alattulis dan sudah ada di data
                        while True:
                            print(
                                "Data sudah ada, apakah tetap akan disimpan? (Y/N)")    #keluar opsi tetap simpan atau tidak
                            opsi = input("Pilihan anda : ")                             #input pilihan opsi
                            opsi = opsi.lower()
                            if opsi == 'y':                                             #bila pilih ya
                                data.append(tambah)                                     #simpan data duplikat dan keluarkan notif
                                print(
                                    "Data duplikat tersimpan dan mengupdate barang")
                                break
                            elif opsi == 'n':                                           #bila pilih tidak
                                print("Data tidak tersimpan")                           #tidak disimpan dan keluarkan notif
                                break
                            else:
                                print("Hanya menerima Y / N")                           #keluar notif apabila selain Y atau N
                                continue
                    else:                                                               #apabila barang tidak ada dalam alattulis
                        print("Data yang anda masukkan tidak termasuk alat tulis")      #keluar notif
                    print("\n"
                        "-----Mini Menu-----\n"
                        "1. masih disini\n"
                        "2. kembali ke menu awal\n"
                        "-----------------------")
                    while True:                                                         #mini menu
                        try:
                            pilihan = int(input("tentukan pilihanmu skrg : "))
                            b = ""
                            if pilihan == 1:
                                b = "masih disini"
                                break
                            elif pilihan == 2:
                                b = "menu awal"
                                break
                            else:
                                print("cuma 1 atau 2 aja bossss. g ade yang lain")
                                continue
                        except:
                            print("cuma 1 atau 2 aja bossss. g ade yang lain")
                            continue

                    if b == "masih disini":
                        continue
                    elif b == "menu awal":
                        break
#================================================================================================================================================================================
            elif perintah == 3:  # menu ubah
                while loop:
                    print("\n------MENGUBAH DATABASE------\n")
                    while True:

                        print("----Input----")
                        x = input("masukkan data yang ingin diubah : ").lower()                 #input barang yang akan ditambahkan dan diseragamkan
                        if x not in data:                                                       #kalau tidak ada di data
                            print("barang tidak ada/barang tidak ditemukan")                    #keluar notif
                            continue
                        else:
                            while True:
                                nama_barang_baru = input(                                       #input barang yang baru dan diseragamkan
                                    "Barang ada. update data menjadi : ").lower()
                                nama_barang_baru = nama_barang_baru.split(' ')                  #barang baru displit
                                balik = []
                                a = 0
                                for i in nama_barang_baru:                                      #pengecekkan barang baru apakah alfabet atau bukan
                                    if not i.isalpha():
                                        balik.clear()
                                        a += 1
                                    else:
                                        balik.append(i)
                                        k = ' '.join(balik)
                                if a > 0:                                                       #apabila tidak alfabet
                                    print(
                                        "Format tulisan tidak sesuai. hanya menerima ALFABET")  #keluar notif
                                    continue
                                else:
                                    nama_barang_baru = k                                        #simpan nama barang baru
                                    break
                            break
                    for j in data:                                                              #pengecekan data
                        if j == x:                                                              #kalau ketemu element data yang namanya sama dengan inputan / var x
                            data[data.index(j)] = nama_barang_baru                              #diganti jadi barang baru
                    print("----Output----")                                                     #keluar notif
                    print("Data Berhasil Diupdate ! ")
                    print("\n"
                        "-----Mini Menu-----\n"
                        "1. masih disini\n"
                        "2. kembali ke menu awal\n"
                        "-----------------------")
                    while True:                                                                 #mini menu
                        try:
                            pilihan = int(input("tentukan pilihanmu skrg : "))
                            b = ""
                            if pilihan == 1:
                                b = "masih disini"
                                break
                            elif pilihan == 2:
                                b = "menu awal"
                                break
                            else:
                                print("cuma 1 atau 2 aja bossss. g ade yang lain")
                                continue
                        except:
                            print("cuma 1 atau 2 aja bossss. g ade yang lain")
                            continue

                    if b == "masih disini":
                        continue
                    elif b == "menu awal":
                        break
#================================================================================================================================================================================
            elif perintah == 4:  # menu hapus
                while loop:
                    print("\n------MENGHAPUS DATABASE------\n")
                    print("----Input----")
                    barang = input("Masukkan barang yang akan dihapus : ")  #input barang
                    barangsplit = barang.split()                            #split string untuk item yang lebih dari 2 kata
                    for a in barangsplit:                                   #for untuk cek apakah hasil split variabel barang adalah seluruhnya alfabet
                        if not a.isalpha():
                            print("Tidak menerima selain alfabet")          #print text dan keluar dari loop pengecekan alfabet
                            break
                    else:
                        if barang.lower() in data:                          #cek apakah variabel barang ada di list data
                            data2 = list(data)                              #create new list sementara untuk looping
                            for a in data2:
                                if a == barang.lower():
                                    data.remove(a)                          #hapus element dalam list jika ada yang sama dengan var barang
                            print("----Output----")                         #print output setelah berhasil
                            print("Data Berhasil Dihapus ! ")
                        else:
                            print("----Output----")                         #print output bila barang tidak ada dalam list data
                            print("Barang tidak ditemukan")
                    print("\n"                                              #print mini menu
                        "-----Mini Menu-----\n"
                        "1. masih disini\n"
                        "2. kembali ke menu awal\n"
                        "-----------------------")    
                    while True:                                             #mini menu
                        try:
                            pilihan = int(input("tentukan pilihanmu skrg : "))
                            b = ""
                            if pilihan == 1:
                                b = "masih disini"
                                break
                            elif pilihan == 2:
                                b = "menu awal"
                                break
                            else:
                                print("cuma 1 atau 2 aja bossss. g ade yang lain")
                                continue
                        except:
                            print("cuma 1 atau 2 aja bossss. g ade yang lain")
                            continue
                    if b == "masih disini":
                        continue
                    elif b == "menu awal":
                        break
#================================================================================================================================================================================
            elif perintah == 5:  # exit
                utama = False
            else:
                print("Masukkan angka yang sesuai dengan menu")
        except:
            print("Hanya masukkan angka sesuai dengan pilihan menu")
