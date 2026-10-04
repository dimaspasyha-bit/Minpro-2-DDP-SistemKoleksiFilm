# Minpro-2-DDP-SistemKoleksiFilm

### Nama = Dimas Surya Pasyha

### NIM = 2609116044

### Kelas = B

# SISTEM KOLEKSI FILM

Di program saya sebelumnya, saya buat sistem koleksi film "pribadi" dan sekarang saya bikin menjadi sistem koleksi film yang dapat di akses oleh pelanggan atau orang lain. jadi saya dapat memberikan rekomendasi film film yang sedang booming lalu menyebarkan nya kedalam koleksi saya.

Jadi program baru ini adalah sistem dimana terdapat dua role yaitu admin yang merupakan pemilik dari koleksi film, dan user yang memakai koleksi tersebut sebagai acuan film apa yang harus dia tonton. Lalu user dapat merating film-film dari koleksi admin, dengan itu admin dapat melakukan evaluasi tentang jenis film seperti apa yang disukai oleh pengikut koleksi dirinya. Selayaknya admin, mereka dapat menghapus, menambahkan, dan mengganti koleksi filmnya dia sendiri, namun admin tidak dapat memberi rating terhadap koleksinya, karena jika admin memberi rating terhadap koleksinya sendiri, rating tersebut berkemungkinan untuk dianggap "subjektif" bukan "objektif".

## 1. Penjelasan Kode Program

#### A. Tahap pembuatan function (def) dan dictionary

<img width="290" height="122" alt="image" src="https://github.com/user-attachments/assets/c0c85358-bcb6-4236-b218-f7a60b1d4bf8" />

Penjelasan: disini saya menggunakan 2 library yaitu prettytable dan os. Prettytable untuk bikin table di koleksi film dan OS untuk membersihkan layar terminal. Lalu saya juga bikin 2 dictionary, yang pertama untuk login dan yang kedua untuk koleksi film.


<img width="342" height="75" alt="image" src="https://github.com/user-attachments/assets/6ee3c92f-e155-4c0f-89e8-ed23e78bc35c" />

Penjelasan: lalu saya buat banyak function, function pertama yang saya buat untuk menampilkan koleksi. lalu seperti yang saya bilang seblumnya saya pakai library prettytable untuk membuat table dikoleksi film. Terus itu ada for idx in enumerate "start=1" itu agar python membaca nomor dari angka 1, bukan 0 lagi.

<img width="314" height="64" alt="image" src="https://github.com/user-attachments/assets/b9fa131d-5016-4393-b276-4c2400b8d086" />


Penjelasan: Saya buat function untuk menambahkan film ke dalam koleksi. Ya seperti biasa buat variable judul dan genre, lalu saya menggunakan .append untuk menambahkannya kedalam dictionary koleksi_film. oiya karena admin tidak boleh memasukkan rating, jadi untuk ratingnya harus kita set default 0.0

<img width="293" height="191" alt="image" src="https://github.com/user-attachments/assets/ca78c913-3ef4-424a-a808-000468d33091" />

Penjelasan: Lalu masuk ke pembuatan function mengganti daftar koleksi, di awal saya memanggil function tampilkan_koleksi () agar users dapat melihat kira kira daftar mana yang ingin dia ubah. lalu ada "nomor_ubah -1" itu agar python tidak menghitung dengan cara indeks dari 0, karena jika python menghitung dari 0 maka saat saya input film nomor 2, pasti yang terubah adalah film nomor 1, oleh karena itu harus pakai -1. terus juga untuk mengubah kayak yang pernah diajarin, memanggil key nya dengan [] dan mengganti nya dengan value baru yang kita buat dalam key tersebut. Oiya saya disini banyak menggunakan try dan except ValueError agar ketika kita menginput selain angka program tidak langsung berhenti.

<img width="306" height="142" alt="image" src="https://github.com/user-attachments/assets/b4fd48c6-c58f-460b-b71c-eca809586dc8" />

penjelasan: Lalu function untuk menghapus film, oiya saya lupa bahwa dalam program kali ini saya sering menggunakan kode "diantara" seperti contohnya 1<= nomor_pilih <= len(koleksi_film), itu artinya ketika nomor pilih saya dari rentang 1 sampai len itu maksudnya angka/data yang ada di dictionary saya. Lalu untuk menghapus saya menggunakan .pop dengan maksud value dari film itu (judul) dapat saya munculkan kembali di pemberitahuan (print) menggunakan f string lalu kurung kurawal {}

<img width="433" height="218" alt="image" src="https://github.com/user-attachments/assets/2a6a9685-9438-43cf-acea-74b30d95fc2a" />

Penjelasan: lalu ini def/function yang terakhir yaitu untuk memberi rating ke koleksi film. Kurang lebih sama seperti sebelum sebelumnya, paling yang beda itu saya bisa bisa memanggil value didalam string dengan cara menggunakan ['key'] didalam kurung kurawal. terus juga yang beda saya menggunakan tipe data float karena biasanya rating itu kan bentuknya desimal bukan bilangan bulat.

#### B. Pemanggilan def/function kedalam menu user dan admin

<img width="229" height="190" alt="image" src="https://github.com/user-attachments/assets/a52f19d7-7c38-449a-bf2b-5234be9c23cd" />
<img width="242" height="136" alt="image" src="https://github.com/user-attachments/assets/5f0278dc-2169-4c97-9f16-2686adf77524" />

Penjelasan: Disini saya menggunakan pengulangan while true dan sama sama mengakhirinya dengan break. lalu saya disitu menggunakan variable pilihan dengan logika if lalu disetiap if dan elif nya kita panggil function function yang telah dibuat sebelumnya.

<img width="372" height="307" alt="image" src="https://github.com/user-attachments/assets/43461468-6595-46f7-9836-f789dd96611b" />

Penjelasan: karena menu login adalah menu utama/yang paling pertama keluar, maka kita buat lah functionnya. terus seperti yang saya bilang tadi disinilah saya menggunakan import os untuk membersihkan layar dari terminal, dengan os.system('cls' if os.name == 'nt' else 'clear') . Lalu saya buat variable kesempatan = 3 agar nantinya bisa dibuat proses agar kesempatan login dari users itu ada 3 kali kesempatan (jika salah). for percobaan in range(1, kesempatan + 1) lalu for ini in range "kesempatan + 1" itu maksudnya agar kesempatan berakhir saat percobaan ke 3, karena itu kalau kita terjemahkan jadinya (1,4) sedangkan dalam python jika ada perhitungan seperti itu, maka dia berhenti sebelum 4. lalu buat variabel login nyaa, terus logika if dalam penentuan role, jadi memanggil function dari menu admin dan menu user. return False Jika loop selesai 3 kali dan tidak ada login yang berhasil, program akan keluar dari fungsi login() dan menampilkan pesan bahwa kesempatan telah habis, sama return True juga agar function dari login() juga berhasil. oiya disitu juga saya menggunakan operator pengurangan untuk sisa, jadi pengurangan dari kesempatan dapat terhitung.

#### C. Perulangan utama/pertama

<img width="209" height="71" alt="image" src="https://github.com/user-attachments/assets/54c1d8fa-8fdc-4e53-af45-f1ec73043f2f" />

Penjelasan: menggunakan while True, lalu memanggil function login(), dan disitu juga bisa mengulang dengan pilihan y/n ketika usn atau pw salah. maksud dari != y itu maksudnya jika tidak sama dengan y maka n gitu. Lalu jika n maka program berhenti.

## 2. Output

#### A. Admin
<img width="238" height="68" alt="image" src="https://github.com/user-attachments/assets/a7357945-422d-4b2b-9824-2809b45f7b2f" />

Menu 2 (tampilkan koleksi) + terjadi pengulangan


<img width="184" height="191" alt="image" src="https://github.com/user-attachments/assets/794d2093-1722-494a-ad14-3171a142609b" />

Menu 1 (tambah koleksi) + pengecekan ulang koleksi + terjadi pengulangan

<img width="191" height="244" alt="image" src="https://github.com/user-attachments/assets/6cdedd28-c363-4360-9d7b-072403b9cc69" />

Menu 3 (mengubah daftar) + Tampilan setelah diubah + terjadi perulangan

<img width="208" height="287" alt="image" src="https://github.com/user-attachments/assets/8d44a330-8fcb-4db9-ac17-98c9bdb5a560" />

Menu 4 (menghapus film) + pengecekan ulang koleksi + terjadi pengulangan

<img width="220" height="292" alt="image" src="https://github.com/user-attachments/assets/8eefaa96-899c-4abd-8923-17e14e4ab517" />

Menu 5 (logout), jika jawab "n",  jika jawab "y", maka akan masuk ke menu login lagi

<img width="215" height="92" alt="image" src="https://github.com/user-attachments/assets/dc1730a7-0430-48ff-985a-8ec2b5b1c015" />

#### B. user
<img width="200" height="131" alt="image" src="https://github.com/user-attachments/assets/d99c171f-ce06-47cf-b4a5-5fa4f843e9b5" />

Menu 1 (tampilkan koleksi) + terjadi pengulangan + data yang dimasukkan oleh admin masih tersimpan jika sebelumnya logout dari role admin.

<img width="214" height="179" alt="image" src="https://github.com/user-attachments/assets/af6cf20d-e627-4e92-bace-141eac6af775" />

Menu 2 (beri rating) + pengecekan ulang koleksi + terjadi perulangan

<img width="215" height="266" alt="image" src="https://github.com/user-attachments/assets/03ec39e3-6dee-4583-828f-78443f8b1465" />

Menu 3 (logout) y/n, jika menginput "y" maka akan masuk ke proses login lagi.

<img width="230" height="87" alt="image" src="https://github.com/user-attachments/assets/3646a843-c2ca-4dda-9620-c4b08758091f" />

#### C. uji tes try except ValueError
<img width="202" height="188" alt="image" src="https://github.com/user-attachments/assets/5f36c6bc-b052-4991-b952-2bc33e3641ae" />

Penjelasan: jika saya menginput huruf di situ, maka akan ada pringatan "harus berupa angka" dan terjadi pengulangan bukan crash/error.

## 3. Penjelasan flowchart

#### A. Login pertama

<img width="169" height="206" alt="image" src="https://github.com/user-attachments/assets/aace229c-654e-4d36-ab92-ee8fc1f82372" />

Penjelasan: input username dan password, menggunakan decision pertama untuk mengecek apakah usn dan pw benar, jika ya masuk ke decision kedua pengecekan role, apakah role merupakan admin? jika iya masuk ke menu admin, jika tidak maka masuk ke menu user.

1. MENU ADMIN
   
<img width="371" height="221" alt="image" src="https://github.com/user-attachments/assets/a5f1345b-afe1-4f15-b8b6-af795e05b370" />

Penjelasan: sesuai dengan program, input 1 = masukkan film baru, input 2 = tampilkan daftar, input 3 = ubah film, input 4 = hapus film, untuk pilihan 1-4 mereka akan kembali lagi ke menu admin dan melanjutkan input pilihan lagi. Namun jika input 5 maka langsung lanjut ke input "apakah ingin login lagi?" y/n.

2. MENU USER

<img width="359" height="213" alt="image" src="https://github.com/user-attachments/assets/c61f5637-df0b-4fdf-bd0e-6fe2d6f9c262" />

Penjelasan: input 1 = tampilkan daftar, input 2 = beri rating, kedua itu akan terjadi pengulangan lagi ke pilihan input. Namun untuk input 3 = logout akan menuju ke tempat yang sama dengan input 5 dari menu admin yaitu "apakah ingin login lagi?" y/n

3. KESALAHAN USERNAME ATAU PASSWORD

<img width="280" height="101" alt="image" src="https://github.com/user-attachments/assets/d2debe91-2cdc-41d0-bb5e-de835282951c" />

Penjelasan: dengan menggunakan persegi panjang (proses) dengan isi "hitung sisa = kesempatan (3) - percobaan" maka terdapat 3 kali percobaan dengan mengkombinasikan decision "apakah sisa=0?" jika tidak maka masih terdapat kesempatan, namun jika iya maka kesempatan habis dan langsung menuju ke input yang sama dengan input 5 "Menu admin" dan input 3 "Menu user" yaitu "apakah ingin login ulang?" y/n.

4. KEPUTUSAN BERPINDAH ROLE/LOGIN ULANG

<img width="355" height="193" alt="image" src="https://github.com/user-attachments/assets/7a2017f3-3dbc-4651-bda8-6821669a1940" />

Penjelasan: input y atau n dan menggunakan decision "apakah input y?" jika tidak maka program akan selesai, namun jika iya maka akan kembali lagi ke atas ke "input username dan password".

gambar jika pilihan y:

<img width="177" height="214" alt="image" src="https://github.com/user-attachments/assets/da0102b4-8d71-4c16-9a11-9747a07238f1" />
