class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}

    def tambah(self, nama, nilai):
        self.data_mahasiswa[nama] = nilai
        print(f"Data mahasiswa '{nama}' berhasil ditambahkan.")

    def tampilkan(self, nama):
        if nama in self.data_mahasiswa:
            print(f"Nama: {nama}, Nilai: {self.data_mahasiswa[nama]}")
        else:
            print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan.")

    def hapus(self, nama):
        if nama in self.data_mahasiswa:
            del self.data_mahasiswa[nama]
            print(f"Data mahasiswa dengan nama '{nama}' Berhasil dihapus. ")
        else:
            print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan. ")
    
    def ubah(self, nama, nilai_baru):
        if nama in self.data_mahasiswa:
            self.data_mahasiswa[nama] = nilai_baru
            print(f"Data mahasiswa '{nama}' berhasil diubah.")
        else:
            print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan.")

daftar_nilai = DaftarNilaiMahasiswa()

while True:
    print("\n=== Menu ===")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Hapus Data Mahasiswa")
    print("4. Ubah Data Mahasiswa")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Masukan nama mahasiswa: ")
        nilai = float(input("masukan nilai mahasiswa: "))
        daftar_nilai.tambah(nama, nilai)

    elif pilihan == "2":
        nama = input("Masukan nama mahasiswa yang ingin ditampilkan: ")
        daftar_nilai.tampilkan(nama)

    elif pilihan == "3":
        nama = input("Masukan nama mahasiswa yang ingin dihapus: ")
        daftar_nilai.hapus(nama)
    
    elif pilihan == "4":
        nama = input("masukan nama mahasiswa yang ingin diubah: ")
        nilai_baru = float(input("Masukan nilai baru: "))
        daftar_nilai.ubah(nama, nilai_baru)


    elif pilihan == "5":
        nama = input("Program selesai. Terima Kasih!")
        break

    else:
        print("Pilihan tidak valid. Silahkan coba lagi.")
