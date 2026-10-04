import os
from prettytable import PrettyTable

users = {
    "admin": {"password": "dimasganteng", "role": "admin"},
    "dimas": {"password": "dimassamarinda", "role": "user"}
}

koleksi_film = [
    {"judul": "The Notebook", "genre": "Horror", "rating": 0.0},
    {"judul": "Doctor Strange", "genre": "Action", "rating": 0.0}
]

def tampilkan_film():
    print("\n=== DAFTAR KOLEKSI FILM ===")
    
    tabel = PrettyTable(["No", "Judul Film", "Genre", "Rating"])
    for idx, film in enumerate(koleksi_film, start=1):
        tabel.add_row([idx, film["judul"], film["genre"], film["rating"]])
    print(tabel)

def tambah_film():
    print("\n--- Tambah Film Baru ---")
    judul = input("Masukkan Judul Film: ")
    genre = input("Masukkan Genre Film: ")
    koleksi_film.append({"judul": judul, "genre": genre, "rating": 0.0})
    print(f"[BERHASIL] Film '{judul}' berhasil ditambahkan!")
    
def ubah_film():
    print("\n --- pilih No. film yang mau diubah --- ")
    tampilkan_film()

    try:
        nomor_ubah = int(input("Nomor film yang ingin diubah: "))
        if 1<= nomor_ubah <= len(koleksi_film):
            film_diubah = koleksi_film[nomor_ubah - 1]
            judul_baru = input("masukkan judul baru: ")
            genre_baru = input("masukkan genre baru: ")
            film_diubah["judul"] = judul_baru
            film_diubah["genre"] = genre_baru
            print("\n (NEW) DAFTAR FILM SETELAH DIUBAH ")
            tampilkan_film()
        else:
            print("nomor tidak valid!!")

    except ValueError:
        print("Pilihan harus berupa angka")

def hapus_film():
    print("\n --- pilih No. film yang ingin dihapus --- ")
    tampilkan_film()

    try:
        nomor_hapus = int(input("Film No. berapa yang ingin dihapus: "))
        if 1<= nomor_hapus <= len(koleksi_film):
            film_dihapus = koleksi_film.pop(nomor_hapus - 1)
            print(f"Film '{film_dihapus['judul']}' berhasil dihapus")
        else:
            print("nomor tidak valid")

    except ValueError:
        print("pilihan harus berupa angka")

def ubah_rating ():
    print("--- Memberi Rating ---")
    tampilkan_film ()

    try:
        nomor_rating = int(input("No. berapa yang anda ingin rating: "))
        if 1<= nomor_rating <= len(koleksi_film):
            film_dipilih = koleksi_film[nomor_rating -1]
            print(f"Memberikan rating untuk film {film_dipilih ['judul']}")

            rating_baru = float(input("Masukkan rating baru (1.0-10.0): "))
            if 1<= rating_baru <=10:
                film_dipilih ["rating"] = rating_baru
                print(f"Anda memberikan rating {rating_baru} untuk film {film_dipilih ['judul']}")
            else:
                print("ERROR masukkan angka  1-10")
        else:
            print("No. film tidak terdapat di daftar")
        
    except ValueError:
        print("Masukkan angka yang valid")


def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Tambah Film")
        print("2. Tampilkan Film")
        print("3. Ubah Film")
        print("4. Hapus Film")
        print("5. Logout")
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            tambah_film()
        elif pilihan == "2":
            tampilkan_film ()
        elif pilihan == "3":
            ubah_film ()
        elif pilihan == "4":
            hapus_film ()
        elif pilihan == "5":
            break

def menu_user():
    while True:
        print("\n=== MENU USER ===")
        print("1. Tampilkan Film")
        print("2. Beri rating")
        print("3. Logout")
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            tampilkan_film()
        elif pilihan == "2":
            ubah_rating ()
        elif pilihan == "3":
            break

def login():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 35)
    print("      SISTEM LOGIN KOLEKSI FILM    ")
    print("=" * 35)

    kesempatan = 3

    for percobaan in range(1, kesempatan + 1):
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"\n[LOGIN BERHASIL] Selamat datang, {username} ({role})!")
            
            if role == "admin":
                menu_admin()
            elif role == "user":
                menu_user()
            
            return True 

        else:
            sisa = kesempatan - percobaan
            if sisa > 0:
                print(f"[ERROR] Username/Password salah! Sisa percobaan: {sisa}\n")
            else:
                print("\n[ERROR] Kesempatan login habis! Akses ditolak.")
    return False

while True:
    login()
    ulang = input("\nIngin login lagi? (y/n): ")
    if ulang != 'y':
        print("Terima kasih!")
        break