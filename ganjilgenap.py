angka = input('Masukkan angka :')

nilai = "Ganjil" if int(angka) % 2 != 0 else "Genap" 
print("Angka tersebut " + nilai)