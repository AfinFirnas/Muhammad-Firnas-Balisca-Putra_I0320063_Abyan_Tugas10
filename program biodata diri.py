print("Program Biodata Diri")

# Ambil Input Dari User
nama = input('Masukkan Nama : ')
umur = input('Masukkan Umur : ')
alamat = input('Masukkan Alamat : ')

# Format Teks
teks = 'Nama: {}\n umur: {}\n Alamat: {}\n'.format(nama,umur,alamat)

# Buka File Untuk Ditulis
file_bio = open('file.txt','w')

# Tulis Teks Ke File
file_bio.write(teks)

# Tutup File
file_bio.close()
