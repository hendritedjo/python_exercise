# libraries
from functools import reduce

# variabel
alattulis = ['kertas', 'buku', 'pulpen', 'pena',
             'pensil', 'penghapus', 'tipex', 'penggaris', 'spidol']
data = {'namabarang': ['pensil', 'pulpen', 'penggaris', 'spidol', 'pensil'],
        'jumlah': [10, 20, 15, 44, 22]}
roman_dic = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
             'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
morse = {
    "0": "-----",  "1": ".----",  "2": "..---",  "3": "...--",  "4": "....-",  "5": ".....",  "6": "-....",  "7": "--...",  "8": "---..",  "9": "----.",
    "a": ".-",  "b": "-...",  "c": "-.-.",  "d": "-..",  "e": ".",  "f": "..-.",  "g": "--.",  "h": "....",  "i": "..",  "j": ".---",  "k": "-.-",  "l": ".-..",  "m": "--",
    "n": "-.",  "o": "---",  "p": ".--.",  "q": "--.-",  "r": ".-.",  "s": "...",  "t": "-",  "u": "..-",  "v": "...-",  "w": ".--",  "x": "-..-",  "y": "-.--",  "z": "--.."
}

data_nama_kota = ["Jakarta Timur", "Cikarang", "Jakarta Barat"]
data_rt = [2, 3, 12]
data_rw = [3, 4, 17]
data_zipcode = [10100, 10000, 22222]
data_latitude = [77.0, 22.1, -47.5]
data_longitude = ["88", "98", "343"]
geo = {
    "Latitude": data_latitude,
    "Longitude": data_longitude
}

daftar_alamat = {
    "Nama Kota": data_nama_kota,
    "RT": data_rt,
    "RW": data_rw,
    "Kode Pos": data_zipcode,
    "Geo": geo
}

data_userID = ["hendri123", "ayas999", "Natali888"]
data_password = ["Tidur123!!", "Kerja987@@", "#7Kurcaci"]
data_email = ["hendri@gmail.com", "ayas@gmail.com", "natali@gmail.com"]
data_nama = ["hendri", "ayas", "natali"]
data_gender = ["pria", "pria", "wanita"]
data_usia = [22, 30, 88]
data_pekerjaan = ["nganggur", "freelance", "ibu rumah tangga"]
data_hobi = [["tidur"], ["berenang", "skydiving"],
             ["masak", "travelling", "makan"]]
data_nomorhp = [8218888999, 8132223456, 8173467813]
DataRegister = {
    "User ID": data_userID,
    "Password": data_password,
    "Email": data_email,
    "Nama": data_nama,
    "Gender": data_gender,
    "Usia": data_usia,
    "Pekerjaan": data_pekerjaan,
    "Hobi": data_hobi,
    "Alamat": daftar_alamat,
    "Nomor HP": data_nomorhp
}

indexuser = 0

ulang = True

# fungsi


def register (): #FUNGSI REGISTER
    global data_nama_kota
    global data_rt
    global data_rw
    global data_zipcode
    global data_latitude
    global data_longitude
    global geo
    global daftar_alamat
    global data_userID
    global data_password
    global data_email
    global data_nama
    global data_gender
    global data_usia
    global data_pekerjaan
    global data_hobi
    global data_nomorhp
    global DataRegister
    
    register = True
    while register :
        print("\n-----MENU REGISTER-----\n")
        while True : #user_id
            userID = input("masukkan user id : ")
            if userID.isalpha() :
                print("User ID harus kombinasi angka dan huruf")
                continue
            elif userID.isnumeric() :
                print("User ID harus kombinasi angka dan huruf")
                continue
            elif userID.isalnum() :
                if len(userID) < 6 :
                    print("minimal 6 karakter")
                    continue
                elif len(userID) > 20 :
                    print("maksimal 20 karakter")
                    continue
                else :
                    for i in data_userID:
                        if i == userID:
                            print("user ID sdh ada")
                            break
                    else :
                        data_userID.append(userID)
                        break
            else :
                print("User ID harus kombinasi angka dan huruf")
                continue
        
        tes_password = 0
        patokan_password = ""
        while tes_password <=3 : #Password
            password = input("masukkan password : ")
            if len(password) < 8:
                print("Password minimal 8 karakter")
            else:
                if password.isalnum():
                    print("karakter harus campuran angka, huruf serta karakter lain")
                else :
                    alphabet_saja = ""
                    spasi = 0
                    for i in password:
                        if i.isalpha ():
                            alphabet_saja += i
                        elif i == " ":
                            spasi += 1
                    if alphabet_saja.isupper():
                        print("Hurufnya harus gede kecil")
                    elif alphabet_saja.islower():
                        print("Hurufnya harus gede kecil")
                    elif spasi > 0:
                        print("G bole ada spasi sayaang")
                    else :
                        data_password.append(password)
                        break
            tes_password+=1
            if tes_password == 3:
                data_userID.pop(data_userID.index(userID))
                print("kesempatan habis")
                patokan_password = "ble"
                break
            else :
                continue
        if patokan_password == "ble":
            return "kembali"
        
        tes_email = 0
        patokan_email = ""
        while tes_email <= 3: #email
            email = input("Masukkan email : ")
            emailsplit = email.split("@")
            if len(emailsplit) != 2:
                print("Email tidak valid, alasan format email salah")
                tes_email+=1
            elif emailsplit[0] == "":
                print("Email tidak valid, alasan format username yang anda masukkan salah")
                tes_email+=1
            elif emailsplit[1] == "":
                print("Email tidak valid, alasan hosting yang anda masukkan salah")
                tes_email+=1
            elif "." not in emailsplit[1]:
                print("Email tidak valid, alasan format email salah")
                tes_email+=1
            else : 
                temp = emailsplit[0]
                if not temp[0].isalnum():
                    print("Email tidak valid, alasan format username yang anda masukkan salah")
                    tes_email +=1
                else:
                    patokan_username = 0
                    for a in temp:
                        if not (a.isalnum() or a == "_" or a == "."):
                            print("Email tidak valid, alasan format username yang anda masukkan salah")
                            patokan_username += 1
                    if patokan_username == 1:
                        tes_email+=1
                    else :
                        temp = emailsplit[1].split(".")
                        if not temp[0].isalnum():
                            print("Email tidak valid, alasan format hosting yang anda masukkan salah")
                            tes_email +=1
                        else:
                            if len(temp) > 3:
                                print("Email tidak valid, alasan format ekstensi yang anda masukkan salah")
                                tes_email +=1
                            else:
                                for a in range(1,len(temp),1):
                                    if not temp[a].isalpha():
                                        print("Email tidak valid, alasan format ekstensi yang anda masukkan salah")
                                        break
                                    if len(temp[a]) > 5 or len(temp[a]) < 2:
                                        print("Email tidak valid, alasan format ekstensi yang anda masukkan salah, max 5 min 2 karakter")
                                        break
                                else:
                                    data_email.append(email)
                                    break
                                tes_email+=1
            if tes_email == 3:
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                print("kesempatan habis")
                patokan_email = "ble"
                break
            else :
                continue
        if patokan_email == "ble":
            return "kembali"

        tes_nama = 0
        patokan_nama = ""
        while tes_nama <= 3 : #Nama
            nama = input("masukkan nama : ").lower()
            masing2_nama = nama.split(" ")
            angka_1 = 0
            for i in masing2_nama :
                if i.isalpha() != True:
                    angka_1 += 1
            if angka_1 > 0 :
                print("format nama salah. hanya menerima alphabet")
            else : 
                data_nama.append(nama)
                break
            tes_nama+=1
            if tes_nama == 3:
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                data_email.pop(data_email.index(email))
                print("kesempatan habis")
                patokan_nama = "ble"
                break
            else :
                continue
        if patokan_nama == "ble":
            return "kembali"
        
        tes_gender = 0
        patokan_gender = ""
        while tes_gender <= 3 : #Gender
            gender = input("pilih gender (pria/wanita) : ").lower()
            if gender != "pria" and gender != "wanita":
                print("hanya menerima pria/wanita")
            else :
                data_gender.append(gender)
                break
            tes_gender +=1
            if tes_gender == 3:
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                data_email.pop(data_email.index(email))
                data_nama.pop(data_nama.index(nama))
                print ("kesempatan habis")
                patokan_gender = "ble"
                break
            else :
                continue
        if patokan_gender == "ble":
            return "kembali"
        
        tes_usia = 0
        patokan_usia = ""
        while tes_usia <= 3 : #Usia
            try:
                usia = int(input("masukkan usia : "))
                if 0 <= usia < 17:
                    print("anda terlalu muda untuk ini")
                elif usia > 80:
                    print("anda terlalu tua untuk ini")
                elif usia < 0 :
                    print("gk boleh minus")
                else:
                    data_usia.append(usia)
                    break
                tes_usia+=1
            except:
                print("hanya menerima angka saja")
                tes_usia+=1
            if tes_usia == 3:
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                data_email.pop(data_email.index(email))
                data_nama.pop(data_nama.index(nama))
                data_gender.pop(data_gender.index(gender))
                print("kesempatan habis")
                patokan_usia = "bleh"
                break
            else :
                continue
        if patokan_usia == "bleh":
            return "kembali"

        tes_pekerjaan = 0
        patokan_pekerjaan = ""
        while tes_pekerjaan <= 3 : #pekerjaan
            pekerjaan = input("masukkan pekerjaan anda : ").lower()
            masing2_pekerjaan = pekerjaan.split(" ")
            angka_2 = 0
            for i in masing2_pekerjaan :
                if i.isalpha() != True:
                    angka_2 += 1
            if angka_2 > 0 :
                print("format pekerjaan salah. hanya menerima alphabet")
            else : 
                data_pekerjaan.append(pekerjaan)
                break
            tes_pekerjaan += 1
            if tes_pekerjaan == 3:
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                data_email.pop(data_email.index(email))
                data_nama.pop(data_nama.index(nama))
                data_gender.pop(data_gender.index(gender))
                data_usia.pop(data_usia.index(usia))
                print("kesempatan habis")
                patokan_pekerjaan = "bleh"
                break
            else :
                continue
        if patokan_pekerjaan == "bleh":
            return "kembali"
        
        tes_hobi = 0
        patokan_hobi = ""
        hobi_1orang = []
        while tes_hobi <= 3 : #hobi
            hobi = input("masukkan hobi anda (hanya alphabet) : ").lower()
            masing2_hobi = hobi.split(" ")
            angka_3 = 0
            for i in masing2_hobi :
                if i.isalpha() != True:
                    angka_3 += 1
            if angka_3 > 0 :
                print("format hobi salah. hanya menerima alphabet")
            else :
                patokan = ""
                hobi_1orang.append(hobi)
                while True :
                    nanya = input("masih mau nambah hobi lagi ? (Y/N)  ").lower()
                    if nanya == "y" :
                        patokan = "iya"
                        break
                    elif nanya == "n" :
                        patokan = "tidak"
                        break
                    else :
                        print("cuma nerima y/n")
                        continue
                if patokan == "tidak":
                    data_hobi.append(hobi_1orang)
                    break
                elif patokan == "iya":
                    continue
            tes_hobi+=1
            if tes_hobi == 3:
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                data_email.pop(data_email.index(email))
                data_nama.pop(data_nama.index(nama))
                data_gender.pop(data_gender.index(gender))
                data_usia.pop(data_usia.index(usia))
                data_pekerjaan.pop(data_pekerjaan.index(pekerjaan))
                print("kesempatan habis")
                patokan_hobi = "bleh"
                break
            else :
                continue
        if patokan_hobi == "bleh":
            return "kembali" 

        print("---ALAMAT---")#################################################

        tes_alamat_nama_kota = 0
        patokan_alamat_nama_kota = ""
        while tes_alamat_nama_kota <= 3 : #Alamat_nama_kota
            nama_kota = input("masukkan nama kota : ").lower()
            masing2_nama_kota = nama_kota.split(" ")
            angka_4 = 0
            for i in masing2_nama_kota :
                if i.isalpha() != True:
                    angka_4 += 1
            if angka_4 > 0 :
                print("format nama kota salah. hanya menerima alphabet")
            else :
                data_nama_kota.append(nama_kota)
                daftar_alamat["Nama Kota"] = data_nama_kota
                break
            tes_alamat_nama_kota+=1
            if tes_alamat_nama_kota == 3:
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                data_email.pop(data_email.index(email))
                data_nama.pop(data_nama.index(nama))
                data_gender.pop(data_gender.index(gender))
                data_usia.pop(data_usia.index(usia))
                data_pekerjaan.pop(data_pekerjaan.index(pekerjaan))
                data_hobi.pop(data_hobi.index(hobi_1orang))
                print("kesempatan habis")
                patokan_alamat_nama_kota = "bleh"
                break
            else :
                continue
        if patokan_alamat_nama_kota == "bleh":
            return "kembali"

        tes_alamat_rt = 0
        patokan_alamat_rt = ""
        while tes_alamat_rt <= 3 : #Alamat_RT
            try :
                rt = int(input("masukkan nomor RT : "))
                if rt > 0:
                    data_rt.append(rt)
                    daftar_alamat["RT"] = data_rt
                    break
                else:
                    print("Angka tidak bisa negatif")
                    tes_alamat_rt += 1
            except:
                print("hanya menerima angka")
                tes_alamat_rt += 1
            if tes_alamat_rt == 3:
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                data_email.pop(data_email.index(email))
                data_nama.pop(data_nama.index(nama))
                data_gender.pop(data_gender.index(gender))
                data_usia.pop(data_usia.index(usia))
                data_pekerjaan.pop(data_pekerjaan.index(pekerjaan))
                data_hobi.pop(data_hobi.index(hobi_1orang))
                data_nama_kota.pop(data_nama_kota.index(nama_kota))
                print("kesempatan habis")
                patokan_alamat_rt = "bleh"
                break
        if patokan_alamat_rt == "bleh":
            return "kembali"
        
        tes_alamat_rw = 0
        patokan_alamat_rw = ""
        while tes_alamat_rw <= 3 : #Alamat_RW
            try :
                rw = int(input("masukkan nomor RW : "))
                if rw > 0 :
                    data_rw.append(rw)
                    daftar_alamat["RW"] = data_rw
                    break
                else:
                    print("Angka tidak bisa negatif")
                    tes_alamat_rw += 1
            except:
                print("hanya menerima angka")
                tes_alamat_rw += 1
            if tes_alamat_rw == 3:
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                data_email.pop(data_email.index(email))
                data_nama.pop(data_nama.index(nama))
                data_gender.pop(data_gender.index(gender))
                data_usia.pop(data_usia.index(usia))
                data_pekerjaan.pop(data_pekerjaan.index(pekerjaan))
                data_hobi.pop(data_hobi.index(hobi_1orang))
                data_nama_kota.pop(data_nama_kota.index(nama_kota))
                data_rt.pop(data_rt.index(rt))
                print("kesempatan habis")
                patokan_alamat_rw = "bleh"
                break
        if patokan_alamat_rw == "bleh":
            return "kembali"
        
        tes_alamat_zipcode = 0
        patokan_alamat_zipcode = ""
        while tes_alamat_zipcode <= 3 : #Alamat_ZIP CODE
            try :
                zipcode = input("masukkan nomor kode pos : ")
                if len(zipcode) == 5 and zipcode.isdigit() and zipcode != "00000":
                    data_zipcode.append(zipcode)
                    daftar_alamat["Kode Pos"] = data_zipcode
                    break
                else:
                    print("Format kodepos salah")
                    tes_alamat_zipcode += 1
            except:
                print("hanya menerima angka")
                tes_alamat_zipcode += 1
            if tes_alamat_zipcode == 3:
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                data_email.pop(data_email.index(email))
                data_nama.pop(data_nama.index(nama))
                data_gender.pop(data_gender.index(gender))
                data_usia.pop(data_usia.index(usia))
                data_pekerjaan.pop(data_pekerjaan.index(pekerjaan))
                data_hobi.pop(data_hobi.index(hobi_1orang))
                data_nama_kota.pop(data_nama_kota.index(nama_kota))
                data_rt.pop(data_rt.index(rt))
                data_rw.pop(data_rw.index(rw))
                print("kesempatan habis")
                patokan_alamat_zipcode = "bleh"
                break
            else :
                continue
        if patokan_alamat_zipcode == "bleh":
            return "kembali"
        
        tes_alamat_geo_latitude = 0
        patokan_alamat_geo_latitude = ""

        while tes_alamat_geo_latitude <= 3 : #Alamat_Geo_Latitude
            latitude = input("masukkan data latitudenya : ")
            try:
                latitude = float(latitude)
                if latitude < -90 or latitude > 90:
                    print("Format latitude salah")
                    tes_alamat_geo_latitude += 1 
                else:
                    data_latitude.append(latitude)
                    geo["Latitude"] = data_latitude
                    daftar_alamat["Geo"] = geo
                    break
            except:
                print("Angka yang anda masukkan salah")
                tes_alamat_geo_latitude += 1        

            if tes_alamat_geo_latitude == 3:
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                data_email.pop(data_email.index(email))
                data_nama.pop(data_nama.index(nama))
                data_gender.pop(data_gender.index(gender))
                data_usia.pop(data_usia.index(usia))
                data_pekerjaan.pop(data_pekerjaan.index(pekerjaan))
                data_hobi.pop(data_hobi.index(hobi_1orang))
                data_nama_kota.pop(data_nama_kota.index(nama_kota))
                data_rt.pop(data_rt.index(rt))
                data_rw.pop(data_rw.index(rw))
                data_zipcode.pop(data_zipcode.index(zipcode))
                print("kesempatan habis")
                patokan_alamat_geo_latitude = "bleh"
                break
            else :
                continue
        if patokan_alamat_geo_latitude == "bleh":
            return "kembali"
        
        tes_alamat_geo_longitude = 0
        patokan_alamat_geo_longitude = ""
        while tes_alamat_geo_longitude <= 3 : #Alamat_Geo_Longitude
            longitude = input("masukkan data longitude : ")

            try:
                longitude = float(longitude)
                if longitude < -180 or longitude > 180:
                    print("Format longitude salah")
                    tes_alamat_geo_longitude += 1 
                else:
                    data_longitude.append(longitude)
                    geo["Longitude"] = data_longitude
                    daftar_alamat["Geo"] = geo
                    break
            except:
                print("Angka yang anda masukkan salah")
                tes_alamat_geo_longitude += 1  

            if tes_alamat_geo_longitude == 3:
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                data_email.pop(data_email.index(email))
                data_nama.pop(data_nama.index(nama))
                data_gender.pop(data_gender.index(gender))
                data_usia.pop(data_usia.index(usia))
                data_pekerjaan.pop(data_pekerjaan.index(pekerjaan))
                data_hobi.pop(data_hobi.index(hobi_1orang))
                data_nama_kota.pop(data_nama_kota.index(nama_kota))
                data_rt.pop(data_rt.index(rt))
                data_rw.pop(data_rw.index(rw))
                data_zipcode.pop(data_zipcode.index(zipcode))
                data_latitude.pop(data_latitude.index(latitude))
                print("kesempatan habis")
                patokan_alamat_geo_longitude = "bleh"
                break
            else :
                continue
        if patokan_alamat_geo_longitude == "bleh":
            return "kembali"

        print("---INPUT ALAMAT SELESAI---")####################################

        tes_nohp = 0
        patokan_nohp = ""
        while tes_nohp <= 3: #no. HP
            nohp = input("masukkan no. HP : ")
            if nohp.isnumeric() is True:
                nohp = int(nohp)
                if len(str(nohp)) < 11 :
                    print("nomornya kurang")
                elif len(str(nohp)) > 13 :
                    print("nomornya kelebihan")
                else :
                    data_nomorhp.append(nohp)
                    break
            else :
                print("harus angka")
            tes_nohp += 1
            if tes_nohp == 3:
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                data_email.pop(data_email.index(email))
                data_nama.pop(data_nama.index(nama))
                data_gender.pop(data_gender.index(gender))
                data_usia.pop(data_usia.index(usia))
                data_pekerjaan.pop(data_pekerjaan.index(pekerjaan))
                data_hobi.pop(data_hobi.index(hobi_1orang))
                data_nama_kota.pop(data_nama_kota.index(nama_kota))
                data_rt.pop(data_rt.index(rt))
                data_rw.pop(data_rw.index(rw))
                data_zipcode.pop(data_zipcode.index(zipcode))
                data_latitude.pop(data_latitude.index(latitude))
                data_longitude.pop(data_longitude.index(longitude))
                print("kesempatan habis")
                patokan_nohp = "bleh"
                break
            else :
                continue
        if patokan_nohp == "bleh":
            return "kembali"
        
        #Menyimpan data/tidak
        simpan = True
        while simpan:
            pilihan_simpan = input("Simpan data ? (Y/N) ").upper()
            if pilihan_simpan == "Y":
                DataRegister["User ID"] = data_userID
                DataRegister["Password"] = data_password
                DataRegister["Email"] = data_email
                DataRegister["Nama"] = data_nama
                DataRegister["Gender"] = data_gender
                DataRegister["Usia"] = data_usia
                DataRegister["Pekerjaan"] = data_pekerjaan
                DataRegister["Hobi"] = data_hobi
                DataRegister["Alamat"] = daftar_alamat
                DataRegister["Nomor HP"] = data_nomorhp
                print("Data tersimpan")
                return "ble"
                # simpan = False
            elif pilihan_simpan == "N":
                data_userID.pop(data_userID.index(userID))
                data_password.pop(data_password.index(password))
                data_email.pop(data_email.index(email))
                data_nama.pop(data_nama.index(nama))
                data_gender.pop(data_gender.index(gender))
                data_usia.pop(data_usia.index(usia))
                data_pekerjaan.pop(data_pekerjaan.index(pekerjaan))
                data_hobi.pop(data_hobi.index(hobi_1orang))
                data_nama_kota.pop(data_nama_kota.index(nama_kota))
                data_rt.pop(data_rt.index(rt))
                data_rw.pop(data_rw.index(rw))
                data_zipcode.pop(data_zipcode.index(zipcode))
                data_latitude.pop(data_latitude.index(latitude))
                data_longitude.pop(data_longitude.index(longitude))
                data_nomorhp.pop(data_nomorhp.index(nohp))
                print("Data Tidak Tersimpan")
                return "kembali"
                # simpan = False
            else :
                print("Hanya menerima Y/N")
                continue


def login():  # FUNGSI LOGIN DAN NUNJUKIN DATA YANG LOGIN
    global indexuser
    global ulang
    rep_login = 0
    # patokan_login = ""
    while rep_login <= 5:
        print("\n-----MENU LOGIN-----\n")
        login_userid = input("masukan user ID : ")
        login_password = input("masukan pass : ")
        if login_userid not in DataRegister["User ID"]:
            rep_login += 1
            print("User ID tidak terdaftar")
        else:
            if login_password != (DataRegister["Password"][DataRegister["User ID"].index(login_userid)]):
                rep_login += 1
                print("password salah")
            else:
                ulang = True
                indexuser = DataRegister["User ID"].index(login_userid)
                # patokan_berhasil_login = ""
                # BERHASIL LOGIN
                # MASUKIN MENU APLIKASINYA============================================
                print("\n-----BERHASIL LOGIN-----\n")
                while ulang:
                    pilihan = main_menu()
                    if pilihan == 1:
                        user_profile(indexuser)
                        
                        while True:
                            try:
                                print("\n"
                              "-----Mini Menu-----\n"
                              "1. Coba menu ini lagi\n"
                              "2. Kembali ke menu utama\n"
                              "--------------------------")
                                opsi = int(
                                    input("Anda telah selesai di menu ini, masukkan pilihan anda: "))
                                if opsi == 1:
                                    user_profile(indexuser)
                                elif opsi == 2:
                                    break
                                else:
                                    print("Maaf, hanya ada pilihan 1 atau 2")
                                    continue
                            except:
                                print("Maaf, hanya ada pilihan 1 atau 2")
                                continue

                    elif pilihan == 2:
                        print(kalkulator())
                        
                        while True:
                            try:
                                print("\n"
                              "-----Mini Menu-----\n"
                              "1. Coba menu ini lagi\n"
                              "2. Kembali ke menu utama\n"
                              "--------------------------")
                                opsi = int(
                                    input("Anda telah selesai di menu ini, masukkan pilihan anda: "))
                                if opsi == 1:
                                    print(kalkulator())
                                elif opsi == 2:
                                    break
                                else:
                                    print("Maaf, hanya ada pilihan 1 atau 2")
                                    continue
                            except:
                                print("Maaf, hanya ada pilihan 1 atau 2")
                                continue

                    elif pilihan == 3:
                        angka = input("Masukan angka romawi atau integer : ")
                        try:
                            if angka.isalpha():
                                angka = angka.upper()
                                for i in angka:
                                    if not(i == 'I' or i == 'V' or i == 'X' or i == 'L' or i == 'C' or i == 'D' or i == 'M'):
                                        print('angka romawi salah')
                                        break
                                    else:
                                        continue
                                print(rom_int(angka))
                            else:
                                angka = int(angka)
                                if angka < 0:
                                    print('gak boleh negatif')
                                else:
                                    print(int_rom(angka))
                        except:
                            print("tidak menerima float")

                        while True:
                            try:
                                print("\n"
                                      "-----Mini Menu-----\n"
                                      "1. Coba menu ini lagi\n"
                                      "2. Kembali ke menu utama\n"
                                      "--------------------------")
                                opsi = int(
                                    input("Anda telah selesai di menu ini, masukkan pilihan anda: "))
                                if opsi == 1:
                                    angka = input(
                                        "Masukan angka romawi atau integer : ")
                                    try:
                                        if angka.isalpha():
                                            angka = angka.upper()
                                            for i in angka:
                                                if not(i == 'I' or i == 'V' or i == 'X' or i == 'L' or i == 'C' or i == 'D' or i == 'M'):
                                                    print('angka romawi salah')
                                                    break
                                                else:
                                                    continue
                                            print(rom_int(angka))
                                        else:
                                            angka = int(angka)
                                            if angka < 0:
                                                print('gak boleh negatif')
                                            else:
                                                print(int_rom(angka))
                                    except:
                                        print("tidak menerima float")
                                elif opsi == 2:
                                    break
                                else:
                                    print("Maaf, hanya ada pilihan 1 atau 2")
                                    continue
                            except:
                                print("Maaf, hanya ada pilihan 1 atau 2")
                                continue

                    elif pilihan == 4:
                        konversi_morse()

                        while True:
                            try:
                                print("\n"
                                      "-----Mini Menu-----\n"
                                      "1. Coba menu ini lagi\n"
                                      "2. Kembali ke menu utama\n"
                                      "--------------------------")
                                opsi = int(
                                    input("Anda telah selesai di menu ini, masukkan pilihan anda: "))
                                if opsi == 1:
                                    konversi_morse()
                                elif opsi == 2:
                                    break
                                else:
                                    print("Maaf, hanya ada pilihan 1 atau 2")
                                    continue
                            except:
                                print("Maaf, hanya ada pilihan 1 atau 2")
                                continue

                    elif pilihan == 5:
                        print(hitung_hari())

                        while True:
                            try:
                                print("\n"
                                      "-----Mini Menu-----\n"
                                      "1. Coba menu ini lagi\n"
                                      "2. Kembali ke menu utama\n"
                                      "--------------------------")
                                opsi = int(
                                    input("Anda telah selesai di menu ini, masukkan pilihan anda: "))
                                if opsi == 1:
                                    print(hitung_hari())
                                elif opsi == 2:
                                    break
                                else:
                                    print("Maaf, hanya ada pilihan 1 atau 2")
                                    continue
                            except:
                                print("Maaf, hanya ada pilihan 1 atau 2")
                                continue

                    elif pilihan == 6:
                        kamus_hari()

                    elif pilihan == 7:
                        konversi_hari()

                        while True:
                            try:
                                print("\n"
                                      "-----Mini Menu-----\n"
                                      "1. Coba menu ini lagi\n"
                                      "2. Kembali ke menu utama\n"
                                      "--------------------------")
                                opsi = int(
                                    input("Anda telah selesai di menu ini, masukkan pilihan anda: "))
                                if opsi == 1:
                                    konversi_hari()
                                elif opsi == 2:
                                    break
                                else:
                                    print("Maaf, hanya ada pilihan 1 atau 2")
                                    continue
                            except:
                                print("Maaf, hanya ada pilihan 1 atau 2")
                                continue

                    elif pilihan == 8:
                        print(faktorial())
                        print("")

                        while True:
                            try:
                                print("\n"
                                      "-----Mini Menu-----\n"
                                      "1. Coba menu ini lagi\n"
                                      "2. Kembali ke menu utama\n"
                                      "--------------------------")
                                opsi = int(
                                    input("Anda telah selesai di menu ini, masukkan pilihan anda: "))
                                if opsi == 1:
                                    print(faktorial())
                                elif opsi == 2:
                                    break
                                else:
                                    print("Maaf, hanya ada pilihan 1 atau 2")
                                    continue
                            except:
                                print("Maaf, hanya ada pilihan 1 atau 2")
                                continue

                    elif pilihan == 9:
                        try:
                            input1 = int(input("Masukkan angka : "))
                            if input1 > 0:
                                deret, jumlah = fibo(input1)
                                print("{} deret angka pertama baris fibonacci adalah {} dan jumlahnya {}".format(
                                    input1, deret, jumlah))
                                print("")
                            else:
                                print("Tidak menerima angka negatif atau nol")
                        except:
                            print("Hanya menerima integer")

                        while True:
                            try:
                                print("\n"
                                      "-----Mini Menu-----\n"
                                      "1. Coba menu ini lagi\n"
                                      "2. Kembali ke menu utama\n"
                                      "--------------------------")
                                opsi = int(
                                    input("Anda telah selesai di menu ini, masukkan pilihan anda: "))
                                if opsi == 1:
                                    try:
                                        input1 = int(
                                            input("Masukkan angka : "))
                                        if input1 > 0:
                                            deret, jumlah = fibo(input1)
                                            print("{} deret angka pertama baris fibonacci adalah {} dan jumlahnya {}".format(
                                                input1, deret, jumlah))
                                            print("")
                                        else:
                                            print(
                                                "Tidak menerima angka negatif atau nol")
                                    except:
                                        print("Hanya menerima integer")
                                elif opsi == 2:
                                    break
                                else:
                                    print("Maaf, hanya ada pilihan 1 atau 2")
                                    continue
                            except:
                                print("Maaf, hanya ada pilihan 1 atau 2")
                                continue

                    elif pilihan == 10:
                        print(caesar())

                        while True:
                            try:
                                print("\n"
                                      "-----Mini Menu-----\n"
                                      "1. Coba menu ini lagi\n"
                                      "2. Kembali ke menu utama\n"
                                      "--------------------------")
                                opsi = int(
                                    input("Anda telah selesai di menu ini, masukkan pilihan anda: "))
                                if opsi == 1:
                                    print(caesar())
                                elif opsi == 2:
                                    break
                                else:
                                    print("Maaf, hanya ada pilihan 1 atau 2")
                                    continue
                            except:
                                print("Maaf, hanya ada pilihan 1 atau 2")
                                continue

                    elif pilihan == 11:
                        setting()

                    elif pilihan == 12:
                        versi1()

                    elif pilihan == 13:
                        print("Anda sudah logout")
                        ulang = False
                        return "kembali"

                # lala = ""
                # while True:
                #     kembali = input(
                #         "\napakah anda ingin keluar ? (Y/N)  ").upper()
                #     if kembali == "Y":
                #         lala = "Y"
                #         break
                #     elif kembali == "N":
                #         lala = "N"
                #         break
                #     else:
                #         print("cuma nerima Y/N g ada yang lain ")
                #         continue
                # if lala == "Y":
                #     return "kembali"
                # elif lala == "N":
                #     continue
        if rep_login == 5:
            print("kesempatan habis")
            return "kembali"
            # break
        else:
            continue


def main_menu():
    while True:
        print("===Main Menu===")
        print("01. User Profile")
        print("02. Kalkulator")
        print("03. Konversi Romawi")
        print("04. Konversi Morse")
        print("05. Perhitungan hari")
        print("06. Kamus Hari")
        print("07. Konversi Jumlah Hari")
        print("08. Nilai Faktorial")
        print("09. Jumlah dan Deret Fibonacci")
        print("10. Caesar Cipher")
        print("11. Setting User")
        print("12. Menu CRUD")
        print("13. Logout")
        input1 = input("Masukkan pilihan (1-13) : ")
        try:
            input1 = int(input1)
            if input1 > 0 and input1 <= 13:
                return input1
            else:
                print("Angka yang anda masukkan salah")
        except:
            print("Hanya menerima angka 1 - 13")


def user_profile(num):
    print("\n====USER PROFILE====")
    for keys, values in DataRegister.items(): #menunjukkan User
        if keys == "Hobi":
            print(keys, ":", ", ".join(values[num]))
        elif keys == "Alamat":
            print("---", keys.upper(), "---")
            for keys_1, values_1 in values.items():
                if keys_1 == "Geo":
                    print("Geo :")
                    for keys_2, values_2 in values_1.items():
                        print("-", keys_2, ":",values_2[num])
                else :
                    print(keys_1, ":",values_1[num])
            print("--------------------")
        elif keys == "Password" or keys == "User ID" or keys == "Email":
            print("", end="")
        elif keys == "Nomor HP":
            print(keys, ": 0", end = "")
            print(values[num])
        else:
            print(keys, ":", values[num])
    print("====================")
    print("")


def kalkulator():
    try:
        x = input("Masukkan angka 1 : ")
        y = input("Masukkan angka 2 : ")
        opr = input("Masukkan operator (hanya terbatas pada + / - * : ")
        x = float(x)
        y = float(y)
        if opr == '+':
            hasil = x + y
            return f"Hasil dari {x} + {y} = {hasil}"
        elif opr == '-':
            hasil = x - y
            return f"Hasil dari {x} - {y} = {hasil}"
        elif opr == '*':
            hasil = x * y
            return f"Hasil dari {x} * {y} = {hasil}"
        elif opr == '/':
            if y == 0:
                return "Tidak bisa dibagi dengan 0"
            else:
                hasil = x / y
                return f"Hasil dari {x} / {y} = {hasil}"
        else:
            return "Maaf, tidak menerima operator yang anda masukkan"

    except ValueError:
        return "Maaf, hanya menerima angka"


def int_rom(Q):
    arabic = {}
    for i, j in roman_dic.items():
        arabic[j] = i
    roman = ""
    for i in arabic.keys():
        count = int(Q / i)
        roman += arabic[i] * count
        Q -= i * count
    return roman


def rom_int(Q):
    i = 0
    number = 0
    while i < len(Q):
        if i < len(Q) and Q[i:i+2] in roman_dic:
            number += roman_dic[Q[i:i+2]]
            i += 2
        else:
            number += roman_dic[Q[i]]
            i += 1
    if int_rom(number) != Q:
        return "Angka romawi tidak valid"
    else:
        return number


def konversi_morse():
    huruf = ""
    Input = input("Masukkan kalimat/kode Morse : ")
    inputnya_itu_kalimat = False

    # Pengecekkan Input adalah Kalimat atau Kode Morse
    for i in Input:
        if i != "." and i != "-" and i != " " and i != "/":
            inputnya_itu_kalimat = True
            break
    else:  # Konversi Kode Morse ke Kalimat
        try:
            # morse2 = dict((y,x) for x,y in morse.items())
            morse2 = {}
            for i, j in morse.items():
                morse2[j] = i
            # kalimat = []
            for x in Input.split(" "):
                kode_kata = x.split("/")
                # if kode_kata[-1] == "":
                #     kode_kata.pop(-1) # Menghapus karakter "" akibat splitting
                for y in kode_kata:
                    huruf = huruf + morse2[y]
                huruf += " "
                # kalimat.append(huruf)
            print(
                f"Kode Morse yg anda masukkan {Input} Hasil konversi menjadi kata-kata adalah :")
            print(huruf)
            # print(" ".join(kalimat).capitalize())
        except:
            print("Format Kode Morse Salah / Kode Morse Tidak Ada")

    # Konversi Kalimat ke Kode Morse
    if inputnya_itu_kalimat == True:
        for x in Input.split(" "):  # Mengecek kalimat hanya alfa + num + space
            if x.isalnum() != True:
                print("Hanya menerima Alfabet, Angka dan Spasi")
                break
        else:
            katakata = Input.lower().split()  # List kata - kata
            morse_kalimat = []
            # for kata in katakata:
            #     morse_kata = ""
            #     for huruf in kata:
            #         morse_kata = morse_kata + morse[huruf] + "/"
            #     morse_kalimat.append(morse_kata)
            # print(" ".join(morse_kalimat))
            for kata in katakata:
                morse_kata = []
                for huruf in kata:
                    morse_kata.append(morse[huruf])
                morse_kalimat.append("/".join(morse_kata))
            print(
                f"Kalimat yg anda masukkan adalah '{Input}'. Kode Morsenya adalah :")
            print(" ".join(morse_kalimat))


def hitung_hari():
    hari = ('senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu')

    try:
        nama = input("Masukkan nama hari : ")
        jumlah = input("Masukkan jumlah hari : ")
        nama = nama.lower()
        jumlah = int(jumlah)
        if nama not in hari:
            return "Nama hari yang anda masukkan salah"
        else:
            i1 = hari.index(nama)
            i2 = (i1 + jumlah) % 7
            return f"Hari ini hari {nama}, {jumlah} hari lagi hari {hari[i2]}"
    except ValueError:
        return "Jumlah tidak bisa desimal maupun string"


def kamus_hari():
    data = {
        "senin": "monday",
        "selasa": "tuesday",
        "rabu": "wednesday",
        "kamis": "thursday",
        "jumat": "friday",
        "sabtu": "saturday",
        "minggu": "sunday"
    }
    while True:
        hari = input("Masukkan nama hari (masukkan 'exit' untuk keluar): ")
        if hari.lower() == 'exit':
            break
        elif hari.isalpha():
            if hari.lower() in data.values():
                for a, b in data.items():
                    if b == hari.lower():
                        print("The day that you choose is {} and in bahasa is {}".format(
                            hari.capitalize(), a.capitalize()))
                        break
            elif hari.lower() in data.keys():
                print("Hari yang anda pilih adalah {} dan dalam bahasa inggris adalah {}".format(
                    hari.capitalize(), data[hari].capitalize()))
            else:
                print("Hari yang anda masukkan salah")
        else:
            print("Tidak menerima selain alfabet")


def konversi_hari():
    try:
        temp = int(input('Masukkan jumlah hari (1 - 4000) : '))
        if (temp > 4000):
            print('Jumlah hari melebihi batas')
        elif (temp < 0):
            print('Jumlah hari di bawah batas')
        else:
            tahun = int(temp/365)
            bulan = int((temp % 365)/30)
            minggu = int(((temp % 365) % 30)/7)
            hari = int((((temp % 365) % 30) % 7))
            print('{:02d} tahun {:02d} bulan {:02d} minggu {:02d} hari'.format(
                tahun, bulan, minggu, hari))
    except:
        print('Jumlah hari tidak bisa menerima string atau angka desimal')


def faktorial():
    try:
        num = int(
            input("Masukkan angka yang ingin diketahui nilai faktorialnya : "))
        if num <= 0:
            return "Maaf, tidak menerima 0 dan negatif"
        else:
            result = 1
            for num in range(2, num + 1):
                result *= num
            return f"Angka {num}, nilai faktorialnya adalah {result}"
    except ValueError:
        return "Maaf, hanya menerima integer"


def fibo(num):
    fibo = []
    if num == 1:
        fibo.extend([0, 1])
    elif num == 2:
        fibo.extend([0, 1, 1])
    else:
        fibo.extend([0, 1, 1])
        for a in range(3, num+1):
            fibo.append(fibo[a-1]+fibo[a-2])
    return " ".join(map(str, fibo)), reduce(lambda x, y: x+y, fibo)


def caesar():
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    k = []
    try:
        kata = input("Masukkan kata : ").lower()
        angka = int(input("Masukkan angka : "))
        if not kata.isalpha():
            return "Maaf, kata hanya menerima kata yang terdiri dari alfabet"
        else:
            for i in kata:
                a = abc.index(i) + angka
                while a >= 26:
                    a = a - 26
                while a < 0:
                    a = a + 26
                k.append(abc[a])
            hasil = ''.join(k)
            return hasil
    except ValueError:
        return "Maaf, inputan anda tidak sesuai"


def setting():
    while True:
        print("\nUser ID  : {}".format(data_userID[indexuser]))
        print("Password : {}".format(data_password[indexuser]))
        print("Email : {}".format(data_email[indexuser]))
        print("")
        while True:
            print("1. Cetak setting user kembali")
            print("2. Keluar")
            input2 = input("Masukkan pilihan : ")
            if input2 == "1":
                break
            elif input2 == "2":
                print("")
                return
            else:
                print("Pilihan yang dimasukkan salah")


def versi1():
    utama = True
    loop = True
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
                if data == {}:
                    print("Daftar Alat Tulis Masih Kosong")
                # looping di sesuai jumlah element di list namabarang
                for i in range(len(data["namabarang"])):
                    # print element di dalam list sesuai dengan index i
                    print(data["namabarang"][i], data["jumlah"][i])
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
    # ================================================================================================================================================================================
            elif perintah == 2:  # menu tambah
                while loop:
                    print("\n------MENAMBAH DATA------\n")
                    # input barang yang akan ditambahkan
                    tambah = input("Masukkan data yang akan ditambahkan : ")
                    try:
                        stock = int(
                            input("Masukkan stock data yang ditambahkan : "))
                        tambah = tambah.lower()  # input diseragamkan di lower case
                        # apabila barang yang akan ditambahkan ada dalam alattulis dan belum ada di data
                        # tambahkan ke data
                        if tambah in alattulis and tambah not in data['namabarang']:
                            data['namabarang'].append(tambah)
                            data['jumlah'].append(stock)
                            print("Data berhasil ditambahkan")
                        # apabila ada di dalam alattulis dan sudah ada di data
                        elif tambah in alattulis and tambah in data['namabarang']:
                            while True:
                                print(
                                    "Data sudah ada, apakah tetap akan disimpan? (Y/N)")  # keluar opsi tetap simpan atau tidak
                                # input pilihan opsi
                                opsi = input("Pilihan anda : ")
                                opsi = opsi.lower()
                                if opsi == 'y':  # bila pilih ya
                                    # simpan data duplikat dan keluarkan notif
                                    data['namabarang'].append(tambah)
                                    data['jumlah'].append(stock)
                                    print(
                                        "Data duplikat tersimpan dan mengupdate barang")
                                    break
                                elif opsi == 'n':  # bila pilih tidak
                                    # tidak disimpan dan keluarkan notif
                                    print("Data tidak tersimpan")
                                    break
                                else:
                                    # keluar notif apabila selain Y atau N
                                    print("Hanya menerima Y / N")
                                    continue
                        else:  # apabila barang tidak ada dalam alattulis
                            # keluar notif
                            print(
                                "Data yang anda masukkan tidak termasuk alat tulis")
                    except:
                        print("Angka yang anda masukkan salah")
                    print("\n"
                          "-----Mini Menu-----\n"
                          "1. masih disini\n"
                          "2. kembali ke menu awal\n"
                          "-----------------------")
                    while True:  # mini menu
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
    # ================================================================================================================================================================================
            elif perintah == 3:  # menu ubah
                while loop:
                    print("\n------MENGUBAH DATABASE------\n")
                    ubah = True
                    while ubah:
                        print("----Input----")
                        print("1. Ubah jenis barang")
                        print("2. Ubah jumlah barang")
                        print("3. Keluar")
                        input1 = input("Masukkan pilihan : ")
                        if input1 == "1":
                            # input barang yang akan ditambahkan dan diseragamkan
                            print("\n----Input----")
                            x = input(
                                "masukkan barang yang ingin diubah : ").lower()
                            # kalau tidak ada di list namabarang
                            if x not in data["namabarang"]:
                                # keluar notif
                                print("barang tidak ada/barang tidak ditemukan")
                                continue
                            else:
                                while True:
                                    # input barang yang baru dan diseragamkan
                                    nama_barang_baru = input(
                                        "Barang ada. update data menjadi : ").lower()
                                    nama_barang_baru = nama_barang_baru.split(
                                        ' ')  # barang baru displit
                                    h = 0
                                    for i in nama_barang_baru:  # pengecekkan barang baru apakah alfabet atau bukan
                                        if i in alattulis:  # dan apakah termasuk alat tulis atau bukan
                                            h += 1
                                            nama_barang_baru = " ".join(
                                                nama_barang_baru)
                                        else:
                                            break
                                    if h > 0:  # apabila alfabet dan alat tulis,
                                        nama_barang_baru  # simpan nama barang baru
                                        break
                                    else:
                                        # jika bukan alfabet dan alat tulis, keluar notif
                                        print("bukan alat tulis")
                                        continue
                            for j in data["namabarang"]:  # pengecekan data
                                if j == x:  # kalau ketemu element data yang namanya sama dengan inputan / var x
                                    # diganti jadi barang baru
                                    data["namabarang"][data["namabarang"].index(
                                        j)] = nama_barang_baru
                                    ubah = False
                        elif input1 == "2":
                            # input barang yang akan ditambahkan dan diseragamkan
                            print("\n----Input----")
                            x = input(
                                "masukkan barang yang ingin diubah : ").lower()
                            # kalau tidak ada di list namabarang
                            if x not in data["namabarang"]:
                                # keluar notif
                                print("barang tidak ada/barang tidak ditemukan")
                                continue
                            else:
                                y = input("Masukkan angka perubahan stok : ")
                                try:
                                    y = int(y)
                                    for z in range(len(data["namabarang"])):
                                        if data["namabarang"][z] == x.lower():
                                            data["jumlah"][z] += y
                                            if data["jumlah"][z] < 0:
                                                print(
                                                    "Stok tidak bisa lebih kecil dari 0, stok {} diubah menjadi 0".format(x))
                                                data["jumlah"][z] = 0
                                    break
                                except:
                                    print("Hanya menerima angka")
                                    continue
                        elif input1 == "3":
                            ubah = False
                        else:
                            print("Input yang anda masukkan salah")
                    print("----Output----")  # keluar notif
                    print("Data Berhasil Diupdate ! ")
                    print("\n"
                          "-----Mini Menu-----\n"
                          "1. masih disini\n"
                          "2. kembali ke menu awal\n"
                          "-----------------------")
                    while True:  # mini menu
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
    # ================================================================================================================================================================================
            elif perintah == 4:  # menu hapus
                while loop:
                    ubah = True
                    while ubah:
                        print("\n------MENGHAPUS DATABASE------\n")
                        print("----Input----")
                        print("1. Hapus semua barang")
                        print("2. Hapus sebagian stok")
                        print("3. Keluar")
                        input1 = input("Masukkan pilihan : ")
                        if input1 == "1":
                            # input barang
                            while True:
                                confirm = input("Pilihan ini akan menghapus seluruh data nama barang dan stok yang tersimpan, apakah anda yakin? (Y/N) ")
                                if confirm.lower() == "y":
                                    data["namabarang"] = [] #hapus semua data namabarang
                                    data["jumlah"] = [] # hapus semua data stok
                                    print("\nBerhasil menghapus semua data barang dan stok")
                                    break
                                elif confirm.lower == "n":
                                    print("Batal menghapus seluruh data yang tersimpan")
                                    break
                                else:
                                    print("Pilihan yang anda masukkan salah")
                            
                        elif input1 == "2":
                            barang = input("Masukkan barang yang akan dihapus : ")
                            barangsplit = barang.split()  # split string untuk item yang lebih dari 2 kata
                            for a in barangsplit:  # for untuk cek apakah hasil split variabel barang adalah seluruhnya alfabet
                                if not a.isalpha():
                                    # print text dan keluar dari loop pengecekan alfabet
                                    print("Tidak menerima selain alfabet")
                                    break
                            else:
                                # cek apakah variabel barang ada di data keys
                                if barang.lower() in data["namabarang"]:
                                    data2 = list(data["namabarang"])
                                    for a in data2:
                                        if a == barang.lower():  # cari index list sesuai dengan nama barang yang diinput
                                            # hapus element list di dalam jumlah yang indexnya sesuai
                                            data["jumlah"].pop(data["namabarang"].index(a))
                                            # hapus element list di dalam namabarang yang indexnya sesuai
                                            data["namabarang"].remove(a)
                                    print("----Output----")
                                    print("Data Berhasil Dihapus ! ")
                                    break
                                else:
                                    # print output bila barang tidak ada dalam list data
                                    print("----Output----")
                                    print("Barang tidak ditemukan")
                                    continue

                        elif input1 == "3":
                            ubah = False
                            break

                        else:
                            print("Pilihan yang anda masukkan salah")

                    print("\n"  # print mini menu
                            "-----Mini Menu-----\n"
                            "1. masih disini\n"
                            "2. kembali ke menu awal\n"
                            "-----------------------")

                    while True:  # mini menu
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
    # ================================================================================================================================================================================
            elif perintah == 5:  # exit
                utama = False
                print("Sudah keluar dari aplikasi")
            else:
                print("Masukkan angka yang sesuai dengan menu")
        except:
            print("Hanya masukkan angka sesuai dengan pilihan menu")


# program utama
while True:  # KYAA APPS
    try:
        print("\n"
              "-----Selamat Datang di Purwadhika Apps-----\n"
              "1. Register\n"
              "2. Login\n"
              "3. Exit\n"
              "-------------------------------------------")
        perintah = int(input("Masukkan pilihan menu (angkanya) : "))
        if perintah == 1:  # register
            hasil_register = register()
            if hasil_register == "kembali":
                continue
            else:
                print(DataRegister)
                continue
        elif perintah == 2:  # login
            hasil_login = login()
            if hasil_login == "kembali":
                continue
        elif perintah == 3:  # exit
            print("kita keluar skrg")
            break
        else:
            print("Hanya menerima angka dari 1 - 3")
            continue
    except:
        print("hanya menerima angkableble")
        continue

print("\n--------------------")
print("|   di luar hehehe  |")
print("--------------------")
