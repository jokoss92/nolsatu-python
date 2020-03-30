angka = int(input("Masukan urutan bilangan Fibonacci : "))

x1, x2 = 0, 1
hitung = 0

if angka <= 0:
    print("Masukkan bilangan positif")
elif angka == 1:
    print("Bilangan Fibonnaci ke " + str(angka) + " adalah " + str(x1))
else:
    while hitung < angka and angka != 1:
        x3 = x1 + x2
        x1 = x2
        x2 = x3
        hitung += 1
    print("Bilangan Fibonnaci ke " + str(angka) + " adalah " + str(x2-x1))

        