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
1. *PrettyTable* Membuat tabel secara otomatis dan rapi untuk tampilan data yang lebih mudah dibaca.
2. *os* Mengelola interaksi dengan sistem operasi, seperti membersihkan terminal dan manajemen file.
3. *pwinput* Membuat password tidak langsung terlihat saat proses login.
4. *csv* format penyimpanan data berbentuk tabel (baris dan kolom), di mana setiap nilai dipisahkan oleh tanda koma.
## ⚙️ Fitur
### 🔧 Admin
Fitur Yang tersedia untuk Admin:
1. *Menambahkan Obat*: Menambahkan Obat kedalam daftar obat.
2. *Melihat Daftar Obat*: Melihat Daftar Obat dan Sekaligus melihat Obat yang Telah di tambahkan.
3. *Memperbarui Daftar Obat*: Memperbarui informasi Daftar obat yang ada.
4. *Menghapus Daftar Obat*: Menghapus Obat yang tidak Tersedia atau dijual lagi.
### 👤 User
Fitur yang tersedia untuk pengguna biasa atau user:
1. *Melihat Daftar Obat*: Menampilkan Daftar Obat Yang tersedia.
2. *Isi Saldo*: Menambah saldo E-Money untuk digunakan dalam transaksi.
3. *Beli Obat*: Melakukan pembelian Obat dengan saldo E-Money.
4. *Lihat Saldo*: Melihat Saldo yang tersia setelah melakukan transaksi atau setelah menambahkan E-Money saat isi saldo.
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
<img width="669" height="242" alt="Screenshot 2025-10-26 221114" src="https://github.com/user-attachments/assets/f4e3211b-3976-4432-959b-465eb85843fb" />

Tampilan yang pertama kali muncul saat menjalankan program adalah menu utama. Disini terdapat 3 pilihan yaitu Login, Registrasi dan Keluar.

<details>

<details>
<summary><h3>🔑Menu Login</h3></summary>
   
### Login Admin
<img width="593" height="118" alt="Screenshot 2025-10-26 221930" src="https://github.com/user-attachments/assets/36efdb7c-f4c2-4e8d-abca-07080f51e07e" />

Jika ingin masuk ke menu admin masukkan:

username: admin

password: 12345678

Jika benar, tekan enter untuk melanjutkan ke menu.

<img width="445" height="107" alt="Screenshot 2025-10-26 222218" src="https://github.com/user-attachments/assets/f1d4e365-1a50-4935-bf0b-3197b49d24f0" />

jika ada kesalahan dalam memasukan username atau password maka harus mengisi ulang username atau password agar bisa masuk kedalam menu admin.

### Login User
<img width="538" height="136" alt="Screenshot 2025-10-26 223400" src="https://github.com/user-attachments/assets/bd2ca894-c4db-42b1-a1a9-8b926dbb85f1" />

untuk login sebagai user sendiri kita di wajibkan register terlebih dahulu.

contoh:

Username : Kiwah

Password :12345678

Jika benar, tekan enter untuk melanjutkan ke menu

<img width="563" height="121" alt="Screenshot 2025-10-26 223322" src="https://github.com/user-attachments/assets/21fe0eeb-3eb2-4915-a745-e52f508ae474" />

jika ada kesalahan dalam memasukan username atau password maka harus mengisi ulang username atau password agar bisa masuk kedalam menu user.

### Registrasi
<img width="506" height="56" alt="Screenshot 2025-10-26 223904" src="https://github.com/user-attachments/assets/641bd900-f4ca-4264-b537-67603bca6a2e" />

Jika nomor 2 yang diinput di menu utama, maka akan di arahkan untuk registrasi telebih dahulu untuk membuat akun. Pertama masukkan nama akun yang ingin di registrasi.

<img width="718" height="148" alt="Screenshot 2025-10-26 224104" src="https://github.com/user-attachments/assets/ef4449fa-f3d3-4fee-9eaf-6713bc87e863" />

Username tidak boleh lebih dari 10 kata

<img width="463" height="40" alt="Screenshot 2025-10-26 224213" src="https://github.com/user-attachments/assets/bd4878af-9c26-434e-9aa6-08b394eb701b" />

Lalu masukkan password

<img width="710" height="130" alt="Screenshot 2025-10-26 224137" src="https://github.com/user-attachments/assets/4aba6b49-6e74-4d5e-8e62-91271fb96e97" />

untuk password sendiri tidak boleh kurang dari 8 kata.

<img width="378" height="128" alt="Screenshot 2025-10-26 224253" src="https://github.com/user-attachments/assets/e795767e-f441-4c60-9b8d-9ec9548a35aa" />

Jika berhasil maka akan muncul pesan di atas. Tekan enter untuk lanjut.

### Keluar Program
<img width="676" height="89" alt="Screenshot 2025-10-26 224844" src="https://github.com/user-attachments/assets/f5710208-bece-452f-a8b4-aafeb3a9211b" />

Jika nomor 3 yang di input di menu utama, maka program akan berhenti dan menampilkan pesan di atas.

</details>

<details>
<summary><h3>🔧Menu Admin</h3></summary>
<img width="593" height="118" alt="Screenshot 2025-10-26 221930" src="https://github.com/user-attachments/assets/4d39140f-1d5b-4c3e-be10-358f1eff66ac" />

Jika ingin masuk ke menu admin masukkan:

username: admin

password: 12345678

Jika benar, tekan enter untuk melanjutkan ke menu.

<img width="688" height="250" alt="Screenshot 2025-10-26 230225" src="https://github.com/user-attachments/assets/f6b62653-a4fe-40e6-8b72-02b26aaad636" />

Berikut tampilan Menu admin

### Tambah Obat
<img width="540" height="36" alt="Screenshot 2025-10-26 225344" src="https://github.com/user-attachments/assets/4fd53736-7bba-4764-85ff-a210be12c777" />

Jika nomor 1 yang diinput maka akan masuk ke menu menambahkan Obat. Masukkan ID Obat.

<img width="715" height="207" alt="Screenshot 2025-10-26 225400" src="https://github.com/user-attachments/assets/48fd39f6-520a-45e1-8d63-628d59f91fba" />

Jika ID telah terdaftar makan harus memilih ID Lain

<img width="451" height="32" alt="Screenshot 2025-10-26 225429" src="https://github.com/user-attachments/assets/545240a5-ecc8-4fef-9f6d-a795a055eca0" />

Lalu Masukan nama Obat yang ingin di tambahkan.

<img width="753" height="210" alt="Screenshot 2025-10-26 225442" src="https://github.com/user-attachments/assets/47f11a3d-8c17-429f-af1e-96a5b986cd95" />

Nama Obat tidak Boleh Kosong.

<img width="452" height="29" alt="Screenshot 2025-10-26 225512" src="https://github.com/user-attachments/assets/49c2702c-1cd8-4009-9e02-ed52a000f4d1" />

Jika nama Obat sudah diinput maka diarahkan untuk memasukkan harga Obat.

<img width="730" height="193" alt="Screenshot 2025-10-26 225537" src="https://github.com/user-attachments/assets/13aa115d-633f-43b3-9453-055a53e7ada6" />

Harga Obat Tidak Boleh Berupa huruf jika memasukan huruf makan otomatis program akan masuk ke menu admin

<img width="467" height="39" alt="Screenshot 2025-10-26 225617" src="https://github.com/user-attachments/assets/251ce305-737d-4e6c-b1b7-38f99021c332" />

Jika Harga obat sudah diinput Maka diarahkan untuk memasukan Stok Obat

<img width="725" height="192" alt="Screenshot 2025-10-26 225633" src="https://github.com/user-attachments/assets/ea192b06-da11-4506-b959-b294f3e80ddf" />

Stok Obat Tidak Boleh Berupa huruf jika memasukan huruf makan otomatis program akan masuk ke menu admin

<img width="607" height="26" alt="Screenshot 2025-10-26 225659" src="https://github.com/user-attachments/assets/17d8f668-7e3b-421a-8716-4bf487681102" />

Jika Stock obat sudah diinput Maka diarahkan untuk memasukan Tingkatan Obat Yaitu Biasa Atau Keras.

<img width="733" height="182" alt="Screenshot 2025-10-26 225716" src="https://github.com/user-attachments/assets/b6d36e24-1df0-4aa9-a9ac-1041ef78cf24" />

Jika memasukan selain pilihan maka akan otomatis program akan masuk ke menu admin

<img width="731" height="284" alt="Screenshot 2025-10-26 225802" src="https://github.com/user-attachments/assets/61daa9ac-2628-49dc-bad6-34fa4aee645c" />

Jika tingkatan obat telah di tambahkan maka Obat akan terdaftar.


### Lihat Obat

<img width="632" height="426" alt="Screenshot 2025-10-26 231620" src="https://github.com/user-attachments/assets/bf67c3b4-9c47-4c23-b2f0-a86e3ff265fd" />

Jika nomor 2 yang diinput maka akan menampilkan apa saja Obat Yang tersedia dengan tabel yang rapi. Tekan enter untuk melanjutkan.

### Ubah/Perbarui Obat
<img width="568" height="65" alt="Screenshot 2025-10-26 231635" src="https://github.com/user-attachments/assets/4e2e30f1-4383-4851-8e7b-2cc0f5e5a511" />

Jika nomor 3 yang diinput maka akan mengupdet atau menubah Data Obat,Masukan ID obat yang ingin di udah

<img width="778" height="214" alt="Screenshot 2025-10-26 231701" src="https://github.com/user-attachments/assets/9e7982e7-e472-4917-ad0a-c22fa5e27210" />

Apabila memasukkan ID Obat yang tidak ada, maka akan menampilkan pesan diatas

<img width="550" height="25" alt="Screenshot 2025-10-26 231729" src="https://github.com/user-attachments/assets/d5ef8447-769d-434d-9555-5c2b49f47601" />

Jika sudah memasukkan nama produk yang ingin di perbarui, lanjut memasukkan nama obat yang baru. Kosongkan jika tidak jadi mengubah.h.

<img width="562" height="26" alt="Screenshot 2025-10-26 231734" src="https://github.com/user-attachments/assets/a6657253-0758-4043-8bf6-1388f7480a59" />

lanjut memasukkan harga obat yang baru. Kosongkan jika tidak jadi mengubah.

<img width="664" height="23" alt="Screenshot 2025-10-26 231741" src="https://github.com/user-attachments/assets/b69426b1-7ad4-4915-ba72-03a4bc2080a9" />

lanjut memasukkan jumlah obat yang baru. Kosongkan jika tidak jadi mengubah.

<img width="738" height="25" alt="Screenshot 2025-10-26 231751" src="https://github.com/user-attachments/assets/31cff1bd-df04-4519-ab20-663e04e89086" />

lanjut memasukkan tingkatan obat yang baru. Kosongkan jika tidak jadi mengubah.

<img width="762" height="294" alt="Screenshot 2025-10-26 231811" src="https://github.com/user-attachments/assets/98b3f835-f6ee-4d5f-91b0-c3ab553a718d" />

Jika berhasil maka akan menampilkan pesan di atas. Tekan enter untuk lanjut.

### Hapus Obat
<img width="471" height="52" alt="Screenshot 2025-10-26 232747" src="https://github.com/user-attachments/assets/3e64edc0-4c05-4912-8c8c-699dab374fc3" />

Jika nomor 4 yang diinput maka akan masuk ke menu menghapus produk. Masukkan ID Obat yang ingin dihapus

<img width="468" height="163" alt="Screenshot 2025-10-26 232736" src="https://github.com/user-attachments/assets/67b2f98e-2fbe-4ec6-87d5-0d39909788f9" />

Jika berhasil  maka akan menampilkan pesan diatas yang berarti produk sudah dihapus.

</details>

<details>
<summary><h3>👤Menu User</h3></summary>

### Lihat/Tampilkan Data Obat

<img width="833" height="622" alt="image" src="https://github.com/user-attachments/assets/f136f0f2-7c95-444e-a88a-057b0dcc2c2e" />
Menampilkan seluruh data obat dalam bentuk tabel rapi menggunakan PrettyTable. Tujuannya agar User dan Admin dapat melihat daftar obat yang tersedia beserta harganya dan stoknya.

### Isi Saldo

<img width="725" height="329" alt="image" src="https://github.com/user-attachments/assets/e1b1c1fe-c234-4171-b374-dee122c68d11" />

User dapat menambah saldo dengan Batasan Minimal Rp10.000 dan Maksimal Rp5.000.000. Jika ingin menambahkan saldo klik pilihan 2 dan masukkan jumlah saldo yang ingin ditambahkan.

### Lihat Saldo

<img width="781" height="260" alt="image" src="https://github.com/user-attachments/assets/737af675-547b-4ec2-ad7d-336612bfb1c0" />

Jika user ingin melihat jumlah saldonya, klik pilihan 4, maka akan ditampilkan terkait jumlah saldo user tersebut.
