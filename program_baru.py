print('Selamat Datang Di Program Biodata')
print('=================================')

# Ambil Input Dari User
nama = input('Nama : ')
umur = input('umur : ')
alamat = input('alamat : ')

# Format Teks
teks = 'Nama: {}\n umur: {}\n Alamat: {}\n'.format(nama,umur,alamat)

# Buka File Untuk Ditulis
file_bio = open('biodata.txt','a')

# Tulis Teks Ke File
file_bio.write(teks)

# Tutup File
file_bio.close()