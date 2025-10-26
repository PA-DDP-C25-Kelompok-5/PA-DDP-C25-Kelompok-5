# Sistem Manajemen Apotek

## 👥Anggota Kelompok 5
| Nama                      | NIM           | Kelas              |
|---------------------------|---------------|--------------------|
| Fitri Yanti               | 2309116016    | Sistem Informasi C |
| Satria Alfiandi R. Akbar  | 2509116089    | Sistem Informasi C |
| Muhammad Risqy Alpianur   | 2509116101    | Sistem Informasi C |

## 📄Deskripsi Program
Program ini adalah Sistem Manajemen Apotek Sederhana yang dibuat menggunakan bahasa pemrograman Python. Terdapat 2 role utama, yaitu Admin dan User.
Role Admin dapat melakukan proses CRUD (Create, Read, Update, Delete) pada data obat. Sementara itu, User dapat melihat daftar obat dan melakukan transaksi pembelian dengan mudah.

### 🎯 Tujuan
Program ini bertujuan untuk:
- Membuat sistem sederhana untuk mengelola data obat di apotek.
- Mempermudah pencatatan transaksi penjualan obat secara cepat dan akurat.
- Memberikan akses berbeda antara Admin dan User.
- Menampilkan data obat dalam format tabel yang rapi dan mudah dibaca.

## 📚 Library yang Digunakan
Terdapat 4 library yang kami gunakan yaitu:
1. **PrettyTable** Membuat tabel secara otomatis dan rapi untuk tampilan data yang lebih mudah dibaca.
2. **os** Mengelola interaksi dengan sistem operasi, seperti membersihkan terminal dan manajemen file.
3. **pwinput** Membuat password tidak langsung terlihat saat proses login.
4. **csv** format penyimpanan data berbentuk tabel (baris dan kolom), di mana setiap nilai dipisahkan oleh tanda koma.
## ⚙️ Fitur
### 🔧 Admin
Fitur Yang tersedia untuk Admin:
1. **Menambahkan Obat**: Menambahkan Obat kedalam daftar obat.
2. **Melihat Daftar Obat**: Melihat Daftar Obat dan Sekaligus melihat Obat yang Telah di tambahkan.
3. **Memperbarui Daftar Obat**: Memperbarui informasi Daftar obat yang ada.
4. **Menghapus Daftar Obat**: Menghapus Obat yang tidak Tersedia atau dijual lagi.
### 👤 User
Fitur yang tersedia untuk pengguna biasa atau user:
1. **Melihat Daftar Obat**: Menampilkan Daftar Obat Yang tersedia.
2. **Isi Saldo**: Menambah saldo E-Money untuk digunakan dalam transaksi.
3. **Beli Obat**: Melakukan pembelian Obat dengan saldo E-Money.
4. **Lihat Saldo**: Melihat Saldo yang tersia setelah melakukan transaksi atau setelah menambahkan E-Money saat isi saldo.
## Flowchart
<details>
  <summary>1. Flowchart Menu Utama</summary>
<img width="1305" height="1265" alt="Menu utama pa ddp drawio" src="https://github.com/user-attachments/assets/e13ef3c4-3528-4112-bb0d-657f02b4357b" />
</details>

<details>
  <summary>2. Flowchart Menu Admin</summary>
<img width="1496" height="2121" alt="Menu admin pa ddp drawio" src="https://github.com/user-attachments/assets/f5b97230-db3b-4357-9001-a9611b542de4" />
</details>

<details>
  <summary>3. Flowchart Menu User</summary>
<img width="915" height="1595" alt="Menu user pa ddp drawio" src="https://github.com/user-attachments/assets/7d5c9dc7-55b1-422d-94ac-b8e9ff1471e1" />
</details>

## Penjelasan Output Program
<details>
<summary><h3>🏠Menu Utama</h3></summary>
<img width="816" height="561" alt="image" src="https://github.com/user-attachments/assets/62bd5995-b62e-47dd-a4c3-d88c2863368f" />

Menu utama (regis), menampilan utama program. Tiga opsi utama:
a.	Login
b.	Registrasi
c.	Keluar
Tujuannya menjadi titik awal seluruh sistem dijalankan, menjadi pintu utama program dan menentukan alur pengguna: apakah dia ingin login, daftar, atau keluar.

<details>

<details>
<summary><h3>🔑Menu Login</h3></summary>
   
### Login Admin
<img width="806" height="535" alt="image" src="https://github.com/user-attachments/assets/135f7ff1-a608-4a6b-b938-65a974e8d08d" />

yang hanya bisa diakses oleh Admin, berisi:
1.	Tambah obat
2.	Lihat obat
3.	Update obat
4.	Hapus obat
5.	Keluar

### Login User
<img width="806" height="535" alt="image" src="https://github.com/user-attachments/assets/9ef44856-7f37-451d-893b-07dd9c25aa67" />

Mengecek apakah file akun.csv ada, minta input username & password, dan mencocokkan data dari file CSV. Jika cocok maka menampilkan role dan saldo user. Jika Admin maka masuk ke menu_admin(), jika User maka masuk ke menu_user(). Tujuannya sebagai gerbang masuk sistem bagi pengguna terdaftar.

### Registrasi

<img width="828" height="564" alt="image" src="https://github.com/user-attachments/assets/8059b8f5-2ff5-4223-9b0b-f67f7dad3118" />

Memanggil dtuser() agar file akun siap digunakan. Meminta username dan password dari pengguna baru. Mengecek panjang username/password agar sesuai aturan (username maksimal 10 karakter dan password minimal 8 karakter), dan mengecek apakah username sudah ada di CSV. Jika belum, menyimpan data baru ke file akun.csv dengan role default “User” dan saldo awal 0. Tujuannya menambahkan akun baru agar pengguna bisa login dan menggunakan sistem (tanpa register, user tidak bisa berinteraksi dengan sistem).

### Keluar Program
<img width="676" height="310" alt="image" src="https://github.com/user-attachments/assets/c93d5136-fd38-48f4-8cd4-872e03f82a13" />
</details>

<details>
<summary><h3>🔧Menu Admin</h3></summary>

<img width="712" height="548" alt="image" src="https://github.com/user-attachments/assets/bf022b65-4e28-450d-a181-5ee82abfac85" />
menu yang hanya bisa diakses oleh Admin, berisi:
1.	Tambah obat
2.	Lihat obat
3.	Update obat
4.	Hapus obat
5.	Keluar
Tujuannya sebagai panel manajemen data obat, agar Admin bisa mengatur stok dan harga dengan mudah. 

### Tambah Obat
ssan 
penjelasan

ssan 
penjelasan

### Ubah/Perbarui Obat
ssan 
penjelasan

ssan 
penjelasan

### Hapus Obat
ssan 
penjelasan

ssan 
penjelasan

### Keluar dari Menu Admin
ssan 
penjelasan

ssan 
penjelasan
</details>

<details>
<summary><h3>👤Menu User</h3></summary>
ssan 
penjelasan

### Lihat/Tampilkan Data Obat

<img width="833" height="428" alt="image" src="https://github.com/user-attachments/assets/7baa4385-2fb6-4b99-99ed-fd18c6943977" />

### Isi Saldo

<img width="841" height="505" alt="image" src="https://github.com/user-attachments/assets/338a914f-1849-49f1-b7cc-9821101be73c" />
<img width="841" height="211" alt="image" src="https://github.com/user-attachments/assets/f75cf853-8616-43ce-934b-85749b6dfe02" />

User dapat menambah saldo dengan Batasan Minimal Rp10.000 dan Maksimal Rp5.000.000. 

### Beli Obat

<img width="841" height="566" alt="image" src="https://github.com/user-attachments/assets/86250cd4-642c-4c8b-af86-4c213d77a028" />
<img width="837" height="503" alt="image" src="https://github.com/user-attachments/assets/50683790-622a-4141-8640-2aa151dd78cb" />

Menampilkan daftar obat, meminta ID obat & jumlah pembelian, mengecek stok dan saldo cukup atau tidak. Jika valid maka bisa mengurangi stok di stock.csv. dan mengurangi saldo user di akun.csv. Tujuannya sebagai fitur utama bagi User untuk melakukan transaksi pembelian obat menggunakan saldo mereka.

### Lihat Saldo

<img width="835" height="216" alt="image" src="https://github.com/user-attachments/assets/5ca21749-2379-44d5-8680-be73adef266f" />

Menampilkan saldo user saat ini. 

