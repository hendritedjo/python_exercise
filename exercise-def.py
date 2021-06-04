def cekemail(email):
    emailsplit = email.split("@")
    if len(emailsplit) != 2:
        print("Email tidak valid, alasan format email salah")
    elif emailsplit[0] == "":
        print("Email tidak valid, alasan format username yang anda masukkan salah")
    elif emailsplit[1] == "":
        print("Email tidak valid, alasan hosting yang anda masukkan salah")
    elif "." not in emailsplit[1]:
        print("Email tidak valid, alasan format email salah")
    else:
        temp = emailsplit[0]
        if not temp[0].isalnum():
            print("Email tidak valid, alasan format username yang anda masukkan salah")
        else:
            for a in temp:
                if not (a.isalnum() or a == "_" or a == "."):
                    print("Email tidak valid, alasan format username yang anda masukkan salah")
                    break
            else:
                temp = emailsplit[1].split(".")
                if not temp[0].isalnum() and len(temp) <= 3:
                    print("Email tidak valid, alasan format hosting yang anda masukkan salah")
                else:
                    for a in range(1,len(temp),1):
                        if not temp[a].isalpha():
                            print("Email tidak valid, alasan format ekstensi yang anda masukkan salah")
                            break
                        if len(temp[a]) > 5:
                            print("Email tidak valid, alasan format ekstensi yang anda masukkan salah")
                            break
                    else:
                        print("Alamat email yang anda masukkan valid")
                
email = input("Masukkan email : ")
cekemail(email)