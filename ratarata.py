array = []
while True:
    angka = input("Masukan bilangan : ")
    if angka == "x" or angka == "X":
        break
    else:
        array.append(int(angka))
        hasil = sum(array) / len(array)
        print(hasil)


