#buka file
file_puisi = open("puisi", "r")

#baca isi file
puisi = file_puisi.read()

#cetak isi file
print(puisi)

#tutup file
file_puisi.close()