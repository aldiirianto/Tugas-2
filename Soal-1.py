#Membuat Array Kosong
nama = []
no_telp = []

#Membuat Perulangan
pilihan = 1
while pilihan != 0 :
    print ("Selamat Datang!")
    print ("-- Menu --")
    print ("1. Daftar Kontak.")
    print ("2. Tambah Kontak.")
    print ("3. Hapus Kontak.")
    print ("4. Keluar.")
    pilihan = int(input("Pilih menu : "))
    print('')
    print('')
    print('')

    if pilihan == 1 :
        penentu = True #Jika telah ditambahkan kontak baru, maka tampilkan :
        for i in range (len(nama)) :
            if penentu :
                print ("nama\t\tno_telp")
            print (nama[i]['nama'],'\t\t ',no_telp[i]['no_telp'])
            penentu = False #Jika tidak ada data kontak, maka tidak tampilkan apa - apa.
        
    elif pilihan == 2 :  
        print("Silahkan tambah kontak baru.")
        inputnama = input("Masukkan Nama Kontak : ")
        nama.append({'nama'       : inputnama}) #Memasukkan data nama kontak ke dalam list kosong
        inputno = input("Masukkan Nomor Telp  : ")
        no_telp.append({'no_telp' : inputno}) #Memasukkan data no telp kontak ke dalam list kosong
        print("Kontak berhasil ditambahkan!")
            
    elif pilihan == 3 :
        inputnama = input("Masukkan Nama : ") #Memasukkan nama kontak yang akan dihapus
        for i in range (len(nama)) :
            if inputnama == nama[i]['nama'] : #Jika nama kontak yang dihapus tersedia maka:
                print(i)
                del nama[i]
                del no_telp[i]
                print("Kontak berhasil dihapus!")
            else: #Jika nama kontak yang dihapus tidak tersedia maka:
                print("Maaf kontak yang Anda cari tidak tersedia.")
                print('')
                print('')
                print('')
    elif pilihan == 4 : 
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia.")
    print('')
    print('')
    print('')
    
