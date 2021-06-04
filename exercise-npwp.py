input1 = input("Masukkan nomor NPWP : ")
status = ""

def cek(npwp):
    npwpsplit = npwp.split("-")
    if len(npwpsplit) != 2:
        return "1"
    else:
        kiri = npwpsplit[0].split(".")
        kanan = npwpsplit[1].split(".")
        if len(kiri) != 4 or len(kanan) != 2:
            return "1"
        else:
            if len(kiri[0]) != 2 or len(kiri[1]) != 3 or len(kiri[2]) != 3 or len(kiri[3]) != 1 or len(kanan[0]) != 3 or len(kanan[1]) != 3:
                return "1"
            else:
                for a in kiri:
                    if not a.isdigit():
                        return "1"
                else:
                    for a in kanan:
                        if not a.isdigit():
                            return "1"
                    else:
                        if int(kiri[0]) > 9:
                            return "1"
                        elif int(kiri[0]) < 1:
                            return "1"
                        else:
                            if int(kiri[0]) <= 3:
                                status = "Wajib Pajak Badan"
                            elif int(kiri[0]) == 4 or int(kiri[0]) == 6:
                                status = "Wajib Pajak Pengusaha"
                            elif int(kiri[0]) == 5:
                                status = "Wajib Karyawan"
                            elif int(kiri[0]) <= 9:
                                status = "Wajib Pajak Pribadi"
                            return status,kiri,kanan

a = cek(input1)
print(a)
if len(a) == 3:
    print("Kode seri NPWP valid!")
    print("Identitas Wajib Pajak: {} {}".format(a[1][0], a[0]))
    print("Nomor Registrasi: {}.{}".format(a[1][1],a[1][2]))
    print("Alat Pengaman : {}".format(a[1][3]))
    print("Kode KKP : {}".format(a[2][0]))
    print("Status Wajib Pajak: {}".format(a[2][1])) 
else:
    print("Kode seri NPWP tidak valid")      

       