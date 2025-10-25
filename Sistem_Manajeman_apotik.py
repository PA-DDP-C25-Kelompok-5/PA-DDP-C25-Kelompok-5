import os
import pwinput
import csv
from prettytable import PrettyTable

dataharga_obat = "stock.csv"
datauser = "akun.csv"

def dtuser ():
    if not os.path.exists(datauser):
        with open(datauser, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "password", "role", "saldo"])

def hrgaobt():
    if not os.path.exists(dataharga_obat):
            with open(dataharga_obat, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Nama", "Harga", "Jumlah", "Tingkatan"])

def clear():
    os.system("cls")

def register():
    clear()
    dtuser()
    username = input("Masukkan username baru: ")
    if len(username) > 10:
        print("+====================================================================+")
        print("|                Nama Tidak Boleh Lebih Dari 10 Karakter             |")
        print("+====================================================================+")
        return

    password = pwinput.pwinput("Masukkan password: ")
    if len(password) < 8:
        print("+====================================================================+")
        print("|           Harus Lebih Dari 8 Angka atau Huruf                      |")
        print("+====================================================================+")
        return

    with open(datauser, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["username"] == username:
                print("+====================================================================+")
                print("|      Username Sudah Terdaftar, Silahkan Coba Nama Lain             |")
                print("+====================================================================+")
                return

    with open(datauser, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([username, password, "User", "0"])
    print(f"Akun '{username}' berhasil dibuat.\n")

def login():
    clear()
    if not os.path.exists(datauser):
        print("Belum ada akun. Silakan registrasi dulu.")
        return

    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ")

    found = False
    with open(datauser, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                found = True
                role = row["role"]
                saldo = float(row["saldo"])
                print(f"\nBerhasil login sebagai {role}")
                print(f"Selamat datang, {username} | Saldo: Rp {saldo:,.0f}\n")

                if role.lower() == "admin":
                    menu_admin()
                else:
                    menu_user(username,saldo)
                break
    if not found:
        print("Nama atau password salah.\n")

def tambahkan():
    hrgaobt()
    try:
        aid = input("Masukkan ID: ")
        if int(aid) <= 0:
            print("Masukan ID harus berupa angka dan lebih dari 0.")
            return
        
        if os.path.exists(dataharga_obat):
            with open(dataharga_obat, mode="r") as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if row and row[0] == aid:
                        print("\n+====================================================================+")
                        print("|                        ID sudah Terdaftar                          |")
                        print("+====================================================================+\n")
                        return

        nama = input("Masukkan nama obat: ")
        if not nama.strip():
            print("\n+====================================================================+")
            print("|                    Nama Tidak Boleh Kosong                         |")
            print("+====================================================================+\n")
            return


        harga = float(input("Masukkan harga obat: "))
        if harga <= 0:
            print("\n+====================================================================+")
            print("|          Harga tidak boleh kurang dari atau sama dengan 0          |")
            print("+====================================================================+\n")
            return

        jumlah = int(input("Masukkan jumlah stok obat: "))
        if jumlah < 0:
            print("\n+====================================================================+")
            print("|                    Jumlah tidak boleh negatif                      |")
            print("+====================================================================+\n")
            return
        elif len(str(jumlah)) > 10:
            print("\n+====================================================================+")
            print("|             Jumlah tidak boleh lebih dari 10 digit                 |")
            print("+====================================================================+\n")
            return

        tingkat = input("Masukkan tingkatan obat (biasa/keras): ").lower()
        if tingkat not in ["biasa", "keras"]:
            print("\n+====================================================================+")
            print("|            Tingkatan hanya boleh 'biasa' atau 'keras'              |")
            print("+====================================================================+\n")
            return

        with open(dataharga_obat, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([aid, nama, harga, jumlah, tingkat])

        print("\n+====================================================================+")
        print("|                     Obat Berhasil Ditambahkan                      |")
        print("+====================================================================+\n")
    except ValueError:
        print("\n+====================================================================+")
        print("|      Input tidak valid, pastikan harga dan jumlah berupa angka     |")
        print("+====================================================================+\n")
    except KeyboardInterrupt:
        ("")
    except EOFError:
        ("")

def lihat():
    try:
        with open(dataharga_obat, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            table = PrettyTable(["ID", "Nama", "Harga", "Jumlah", "Tingkatan"])
            for row in reader:
                table.add_row(row)
            print(table)
    except FileNotFoundError:
        print("Obat belum terdaftar, silakan tambahkan obat terlebih dahulu.")

def update():
    lihat()
    id_nomor = input("\nMasukkan ID yang mau diupdate: ")
    update_rows = []
    found = False

    try:
        with open(dataharga_obat, mode="r") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if not header:
                print("File kosong, tidak ada data untuk diupdate.")
                return
            
            for row in reader:
                if row[0] == id_nomor:
                    nama = input("Nama baru obat (Enter jika tidak ingin mengubah): ") or row[1]
                    harga_input = input("Harga baru (Enter jika tidak ingin mengubah): ")
                    jumlah_input = input("Jumlah stok baru (Enter jika tidak ingin mengubah): ")
                    tingkat = input("Masukkan tingkatan obat ('biasa'/'keras'),(Enter jika tidak ingin mengubah): ").lower() or row[4]

                    if tingkat not in ["biasa", "keras"]:
                        print("\n+====================================================================+")
                        print("|            Tingkatan hanya boleh 'biasa' atau 'keras'              |")
                        print("+====================================================================+\n")
                        return

                    try:
                        harga = float(harga_input) if harga_input.strip() != "" else float(row[2])
                        jumlah = int(jumlah_input) if jumlah_input.strip() != "" else int(row[3])
                    except ValueError:
                        print("Input angka tidak valid. Pembaruan dibatalkan.")
                        return

                    update_rows.append([id_nomor, nama, harga, jumlah, tingkat])
                    found = True
                else:
                    update_rows.append(row)

    except FileNotFoundError:
        print("Obat belum terdaftar.")
        return

    except ValueError:
        print("\n+====================================================================+")
        print("|      Input tidak valid, pastikan harga dan jumlah berupa angka     |")
        print("+====================================================================+\n")
        return

    if found:
        with open(dataharga_obat, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nama", "Harga", "Jumlah", "Tingkatan"])
            writer.writerows(update_rows)
        print("\n+====================================================================+")
        print("|                      Data berhasil diperbarui                      |")
        print("+====================================================================+\n")
    else:
        print("\n+====================================================================+")
        print("|                      ID obat tidak ditemukan                       |")
        print("+====================================================================+\n")

def hapus():
    lihat()
    id_hapus = input("\nMasukkan ID obat yang mau dihapus: ")
    rows = []
    found = False

    try:
        with open(dataharga_obat, mode="r") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] == id_hapus:
                    found = True
                else:
                    rows.append(row)
    except FileNotFoundError:
        print("Obat belum terdaftar.")
        return

    if found:
        with open(dataharga_obat, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        print(f"\n1Data obat dengan ID '{id_hapus}' berhasil dihapus.\n")
    else:
        print("\n+====================================================================+")
        print("|                      ID obat belum terdaftar                       |")
        print("+====================================================================+\n")

def update_saldo(username, saldo):
    rows = []
    with open(datauser, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["username"] == username:
                row["saldo"] = str(saldo)
            rows.append(row)
    with open(datauser, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["username", "password", "role", "saldo"])
        writer.writeheader()
        writer.writerows(rows)

def isi_saldo(username, saldobaru):
    try:
        tambah = float(input("Masukkan jumlah saldo yang ingin ditambahkan: "))

        if tambah <= 0:
            print("\n+====================================================================+")
            print("|        Jumlah saldo yang ditambahkan harus lebih dari 0            |")
            print("+====================================================================+\n")
            return saldobaru
        
        if tambah < 10000:
            print("\n+====================================================================+")
            print("|     Jumlah saldo yang ditambahkan harus lebih dari Rp.10.000       |")
            print("+====================================================================+\n")
            return saldobaru

        if tambah > 5000000:
            print("\n+====================================================================+")
            print("|       Tidak boleh menambahkan saldo lebih dari Rp 5.000.000        |")
            print("+====================================================================+\n")
            return saldobaru
        
        saldo = saldobaru + tambah
        update_saldo(username, saldo)

        print(f"\nSaldo berhasil ditambahkan! Saldo sekarang: Rp {saldo:,.0f}")
        return saldo

    except ValueError:
        print("\n+====================================================================+")
        print("|     Harap masukkan angka yang valid, bukan huruf atau simbol.      |")
        print("+====================================================================+\n")
        return saldobaru

    except KeyboardInterrupt:
        print("")
        return saldobaru

def lihat_saldo(username):
    with open(datauser, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username:
                print(f"Saldo Anda saat ini: Rp {float(row['saldo']):,.0f}")
                return
    print("Akun tidak ditemukan.")

def beli_obat(username, saldo):
    lihat()
    try:
        id_obat = input("\nMasukkan ID obat yang ingin dibeli: ")
        jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))

        if jumlah_beli <= 0:
            print("\n+====================================================================+")
            print("|                Jumlah pembelian harus lebih dari 0                 |")
            print("+====================================================================+\n")
            return saldo

        rows = []
        total_harga = 0
        found = False

        with open(dataharga_obat, mode="r") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] == id_obat:
                    found = True
                    harga = float(row[2])
                    stok = int(row[3])
                    if jumlah_beli > stok:
                        print("Stok tidak cukup.")
                        return saldo
                    total_harga = harga * jumlah_beli
                    stok -= jumlah_beli
                    row[3] = str(stok)
                rows.append(row)

        if not found:
            print("ID obat tidak ditemukan.")
            return saldo

        if saldo < total_harga:
            print("Saldo tidak cukup.")
            return saldo

        saldo -= total_harga
        update_saldo(username, saldo)

        with open(dataharga_obat, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)

        print(f"\nPembelian berhasil! Total harga: Rp {total_harga:,.0f}")
        print(f"Sisa saldo: Rp {saldo:,.0f}")
        return saldo

    except ValueError:
        print("\n+====================================================================+")
        print("|     Input tidak valid! Masukkan jumlah dalam bentuk angka saja     |")
        print("+====================================================================+\n")
        return saldo

def menu_user(username, saldo):
    while True:
        clear()
        print("\n+====================================================================+")
        print("|                             Menu User                              |")
        print("+====================================================================+")
        print("| [1]. Lihat Daftar Obat                                             |")
        print("| [2]. Isi Saldo                                                     |")
        print("| [3]. Beli Obat                                                     |")
        print("| [4]. Lihat Saldo                                                   |")
        print("| [0]. Keluar                                                        |")
        print("+====================================================================+")
        try:
            pilihan = input("Masukkan pilihan (0-4): ")

            if pilihan == "1":
                lihat()
            elif pilihan == "2":
                saldo = isi_saldo(username, saldo)
            elif pilihan == "3":
                saldo = beli_obat(username, saldo)
            elif pilihan == "4":
                lihat_saldo(username)
            elif pilihan == "0":
                print("Logout berhasil.")
                break
            else:
                print("Masukkan angka yang sesuai.")
            input("\nTekan Enter untuk lanjut...")
        except ValueError:
            print("+====================================================================+")
            print("|         Masukkan huruf dan angka, bukan karakter simbol.           |")
            print("+====================================================================+")
        except KeyboardInterrupt:
            ("")
        except EOFError:
            ("")

def menu_admin():
    clear()
    while True:
        clear()
        print("\n+====================================================================+")
        print("|                             Menu Admin                             |")
        print("+====================================================================+")
        print("| [1]. Tambahkan Obat                                                |")
        print("| [2]. Lihat Daftar Obat                                             |")
        print("| [3]. Updet daftar Obat                                             |")
        print("| [4]. Hapus Obat                                                    |")
        print("| [0]. Keluar                                                        |")
        print("+====================================================================+")
        try:
            pilihan = input("Masukkan pilihan 0-4: ")
            if pilihan == "1":
                tambahkan()
            elif pilihan == "2":
                lihat()
            elif pilihan == "3":
                update()
            elif pilihan == "4":
                hapus()
            elif pilihan == "0":
                print("Logout berhasil.")
                break
            else:
                print("Masukkan angka yang sesuai.")
            input("\nTekan Enter untuk lanjut...")
        except ValueError:
            print("+====================================================================+")
            print("|         Masukkan huruf dan angka, bukan karakter simbol.           |")
            print("+====================================================================+")
        except KeyboardInterrupt:
            ("")
        except EOFError:
            ("")

def regis():
    while True:
        clear()
        print("\n+====================================================================+")
        print("|              Selamat Datang di Sistem Toko Perhiasan               |")
        print("+====================================================================+")
        print("|                            Menu Utama                              |")
        print("+====================================================================+")
        print("| [1]. Login                                                         |")
        print("| [2]. Registrasi                                                    |")
        print("| [3]. Keluar                                                        |")
        print("+====================================================================+")
        try:
            pilihan = input("Pilih opsi: ")
            if pilihan == "1":
                login()
            elif pilihan == "2": 
                register()
                input('Tekan Enter untuk melanjutkan...')
            elif pilihan == "3":
                print("+====================================================================+")
                print("|  Anda berhasil keluar. Terimakasih telah menggunakan pogram ini!   |")
                print("+====================================================================+")
                break
            else:
                print("+====================================================================+")
                print("|                       Pilihan tidak valid!                         |")
                print("+====================================================================+")
                input("Tekan enter untuk melanjutkan.....")    
        except ValueError:
            print("+====================================================================+")
            print("|         Masukkan huruf dan angka, bukan karakter simbol.           |")
            print("+====================================================================+")
        except KeyboardInterrupt:
            ("")
        except EOFError:
            ("")

print(regis())