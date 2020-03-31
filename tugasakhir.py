import csv
import os

csv_filename = 'datas.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("[1] Lihat Data")
    print("[2] Buat Data Baru")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[5] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    
    if(selected_menu == "1"):
        try:
            show_data()
        except FileNotFoundError:
            print("Belum Ada Data")
        finally:
            back_to_menu()
    elif(selected_menu == "2"):
        create_data()
    elif(selected_menu == "3"):
        edit_data()
    elif(selected_menu == "4"):
        delete_data()
    elif(selected_menu == "5"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def show_data():
    clear_screen()
    datas = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            datas.append(row)

    if (len(datas) > 0):
        labels = datas.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t\t {labels[2]}")
        print("-"*34)
        for data in datas:
            print(f'{data[0]} \t {data[1]} \t {data[2]}')
    else:
        print("Belum Ada Data")
    back_to_menu()


def create_data():
    clear_screen()
    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['NAMA', 'KELAS', 'NILAI']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        nama = input("Nama: ")
        kelas = input("Kelas: ")
        nilai = input("Nilai: ")

        writer.writerow({'NAMA': nama, 'KELAS': kelas, 'NILAI': nilai})
        print("Berhasil disimpan!")

    back_to_menu() 

def edit_data():
    clear_screen()
    datas = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            datas.append(row)

    print("NAMA \t KELAS \t\t NILAI")
    print("-" * 32)

    for data in datas:
        print(f"{data['NAMA']} \t {data['KELAS']} \t {data['NILAI']}")

    print("-----------------------")
    nama = input("Masukan nama yang akan diedit: ")
    kelas = input("Masukan kelas yang baru: ")
    nilai = input("Masukan nilai yang baru: ")


    indeks = 0
    for data in datas:
        if (data['NAMA'] == nama):
            datas[indeks]['KELAS'] = kelas
            datas[indeks]['NILAI'] = nilai
        indeks = indeks + 1

    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NAMA', 'KELAS', 'NILAI']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in datas:
            writer.writerow({'NAMA': new_data['NAMA'], 'KELAS': new_data['KELAS'], 'NILAI': new_data['NILAI']}) 

    back_to_menu()



def delete_data():
    clear_screen()
    datas = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            datas.append(row)

    print("NAMA \t KELAS \t\t NILAI")
    print("-" * 32)

    for data in datas:
        print(f"{data['NAMA']} \t {data['KELAS']} \t {data['NILAI']}")

    print("-----------------------")
    nama = input("Hapus nama: ")


    indeks = 0
    for data in datas:
        if (data['NAMA'] == nama):
            datas.remove(datas[indeks])
        indeks = indeks + 1

    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NAMA', 'KELAS', 'NILAI']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in datas:
            writer.writerow({'NAMA': new_data['NAMA'], 'KELAS': new_data['KELAS'], 'NILAI': new_data['NILAI']}) 

    print("Data sudah terhapus")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()