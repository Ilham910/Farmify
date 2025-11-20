#Farmify

import pandas as pd
from datetime import datetime, timedelta
import os
import time
from tabulate import tabulate

def loading():
    print(f"{'Loading...':^22}")
    for i in range(1, 21):
        print("[" + "=" * i + " " * (20 - i) + "]", end="\r")
        time.sleep(0.05)

    time.sleep(0.05)
    clear()

def splash_farmify():
    clear()

    logo = [
        "      ______                _________        ______  __   __   ",
        "     / ____/        ____   / _    _  \  __  / ____/ / /  / /  ",
        "    / /_   ___     / ___\ / / /  / / / /_/ / /_    / /__/ /  ",
        "   / __/ / __  \  / /    / / /  / / / / / / __/    \__   /  ",
        "  / /   / /_/  / / /    / / /__/ / / / / / /     __   / /   ",
        " /_/    \_____/ /_/    /_/      /_/ /_/ /_/      \ \_/ /   ",
        "                                                  \___/    ",
        "                                                           ",
       f"{'F  A  R  M  I  F  Y':^50}",
       f"{'Smart Farm Management System':^50}",
    ]

    for line in logo:
        print(line)
        time.sleep(0.1)

PassAdmin = "admin123"

username = "petugas07"
passpetugas = "PetugasGacor"

def clear():
    os.system('cls')

def Tambah_pekerja():
    kolom = ["ID", "Username", "Password", "Nama Lengkap", "No. Telepon", "Alamat", "ID Lahan"]

    try:
       df = pd.read_csv('data_petugas.csv', dtype={"ID Lahan": "Int64"})
    except FileNotFoundError:
       df = pd.DataFrame(columns=kolom)
       df.to_csv('data_petugas.csv', index=False)

    if df.empty:
        new_id = 1
    else:
        new_id = df['ID'].max() + 1

    while True:
        print("\n=== Menambah Petugas Baru ===")
        user = input("Username: ")
        clear()
        print("\n=== Menambah Petugas Baru ===")
        pw = input("Password: ")
        clear()
        print("\n=== Menambah Petugas Baru ===")
        nama = input("Nama Lengkap: ")
        clear()
        while True:
            print("\n=== Menambah Petugas Baru ===")
            telepon = input("No. Telepon: ")

            if telepon.isdigit() == False:
                clear()
                print("No. telepon harus berisi angka!")
                continue
            elif telepon.isdigit() == True:
                clear()
                break
        print("\n=== Menambah Petugas Baru ===")
        alamat = input("Alamat: ")

        clear()

        print(f"Username : {user}")
        print(f"Password : {pw}")
        print(f"Nama Lengkap : {nama}")
        print(f"No. Telepon : {telepon}")
        print(f"Alamat : {alamat}")
        
        while True:
            konfirm = input("\nApakah data pekerja sudah benar (y/n): ")
            if konfirm == "y":
                clear()
                selesai = True
                break
            elif konfirm == "n":
                clear()
                selesai = False
                break
            else:
                print("Pilihan tidak valid!")
                continue
        
        if selesai == True:
            clear()
            break

    print("===== Lahan yang tersedia =====")
    print("1. Lahan 1")
    print("2. Lahan 2")
    print("3. Lahan 3")

    while True:
        pilih_lahan = input("\nPilih lahan untuk pekerja: ")
        
        if pilih_lahan == "1":
            id_lahan = 1
            break
        elif pilih_lahan == "2":
            id_lahan = 2
            break
        elif pilih_lahan == "3":
            id_lahan = 3
            break
        else:
            print("Pilihan tidak valid!")

    df = pd.read_csv('data_petugas.csv', dtype={"ID Lahan": "Int64"})
    df = pd.concat([df, pd.DataFrame([[new_id ,user, pw, nama, telepon, alamat, id_lahan]], columns=kolom)], ignore_index=True)
    df["ID Lahan"] = df["ID Lahan"].astype("Int64")
    df.to_csv('data_petugas.csv', index=False)

def update_petugas():
    df = pd.read_csv('data_petugas.csv')
    print("========== Daftar Pekerja ==========")
    print(tabulate(df.loc[:, ["ID", "Nama Lengkap"]], headers=["ID", "Nama Lengkap"], tablefmt='fancy_grid', showindex=False))
    while True:
        df = pd.read_csv('data_petugas.csv')

        while True:
            df = pd.read_csv('data_petugas.csv')
            id = (input('Masukkan ID petugas yang ingin diupdate ("tekan q untuk kembali"): '))

            if id == "q":
                break

            if not id.isdigit():
                clear()
                df = pd.read_csv('data_petugas.csv')
                print("========== Daftar Pekerja ==========")
                print(tabulate(df.loc[:, ["ID", "Nama Lengkap"]], headers=["ID", "Nama Lengkap"], tablefmt='fancy_grid', showindex=False))
                print("\nID harus berupa angka!\n")
            else:
                break

        if id == "q":
            break

        id = int(id)

        if id not in df['ID'].values:
            clear()
            df = pd.read_csv('data_petugas.csv')
            print("========== Daftar Pekerja ==========")
            print(tabulate(df.loc[:, ["ID", "Nama Lengkap"]], headers=["ID", "Nama Lengkap"], tablefmt='fancy_grid', showindex=False))
            print("\nID tidak ditemukan!\n")
        elif id in df['ID'].values:
            break
    
    while True:
        if id == "q":
            break
        clear()
        petugas = df[df['ID'] == id].iloc[0]
        print("\nData saat ini:")
        print(f"1. Username      : {petugas['Username']}")
        print(f"2. Password      : {petugas['Password']}")
        print(f"3. Nama Lengkap  : {petugas['Nama Lengkap']}")
        print(f"4. No. Telepon   : {petugas['No. Telepon']}")
        print(f"5. Alamat        : {petugas['Alamat']}")
        print("6. Keluar")

        pilihan = input("\nPilih data yang ingin diubah: ")

        if pilihan == "1":
            new_username = input("\nUsername baru: ")
            df.loc[df['ID'] == id, 'Username'] = new_username
            df.to_csv('data_petugas.csv', index=False)
            clear()
            print("Data berhasil diubah!")
        elif pilihan == "2":
            new_password = input("\nPassword baru: ")
            df.loc[df['ID'] == id, 'Password'] = new_password
            df.to_csv('data_petugas.csv', index=False)
            clear()
            print("Data berhasil diubah!")
        elif pilihan == "3":
            new_nama     = input("\nNama lengkap baru: ")
            df.loc[df['ID'] == id, 'Nama Lengkap'] = new_nama
            df.to_csv('data_petugas.csv', index=False)
            clear()
            print("Data berhasil diubah!")
        elif pilihan == "4":
            while True:
                try:
                    new_telp = int(input("\nNo. telepon baru: "))
                    break
                except Exception:
                    print("\nNo. telepon harus berupa angka!")
                    continue
            df.loc[df['ID'] == id, 'No. Telepon'] = new_telp
            df.to_csv('data_petugas.csv', index=False)
            clear()
            print("Data berhasil diubah!")
        elif pilihan == "5":
            new_alamat   = input("\nAlamat baru: ")
            df.loc[df['ID'] == id, 'Alamat'] = new_alamat
            df.to_csv('data_petugas.csv', index=False)
            clear()
            print("Data berhasil diubah!")
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid!")
            continue

    df.to_csv('data_petugas.csv', index=False)
    clear()
    print("\n✔ Data petugas berhasil diperbarui!")


def hapus_petugas():
    while True:
        df = pd.read_csv('data_petugas.csv')
        print("========== Daftar Pekerja ==========")
        print(tabulate(df.loc[:, ["ID", "Nama Lengkap"]], headers=["ID", "Nama Lengkap"], tablefmt='fancy_grid', showindex=False))

        while True:
            ID = (input('Masukkan ID petugas yang ingin dihapus (tekan "q" untuk kembali): '))

            if ID == "q":
                break

            if not ID.isdigit():
                clear()
                print("ID harus berupa angka!\n")
                input("Tekan enter untuk melanjutkan...")
                clear()
                df = pd.read_csv('data_petugas.csv')
                print("========== Daftar Pekerja ==========")
                print(tabulate(df.loc[:, ["ID", "Nama Lengkap"]], headers=["ID", "Nama Lengkap"], tablefmt='fancy_grid', showindex=False))
            else:
                break

        if ID == "q":
            break

        ID = int(ID)

        if ID not in df['ID'].values:
            clear()
            print("ID tidak ditemukan!\n")
            input("Tekan enter untuk melanjutkan...")
            clear()
        else:
            ID = int(ID)
            df = df[df['ID'] != ID]
            df.to_csv('data_petugas.csv', index=False)
            clear()
            print("Pekerja berhasil dihapus!\n")

def biaya_produksi():
    kolom = ["Tanggal Beli", "Nama Barang", "Total Barang", "Harga Barang (Rp.)", "Harga Total (Rp.)"]

    try:
       df = pd.read_csv('biaya_produksi.csv')
    except FileNotFoundError:
       df = pd.DataFrame(columns=kolom)
       df.to_csv('biaya_produksi.csv', index=False)

    tanggal_beli = datetime.now().strftime("%d-%m-%Y")

    beli_pupuk = 0
    beli_benih_padi = 0
    beli_benih_kacang = 0
    beli_benih_jagung = 0
    beli_pestisida = 0

    while True:
        print("\n=== Barang yang ingin dibeli ===")
        print("1. Pupuk Organik (1 kg) - Rp 10.000")
        print("2. Benih Padi (1 kg) - Rp 30.000")
        print("3. Benih Kacang (1 kg) - Rp 30.000")
        print("4. Benih Jagung (1 kg) - Rp 45.000")
        print("5. Pestisida (50 ml) - Rp 25.000")
        print("6. Selesai")

        beli = input("Pilih barang yang ingin dibeli: ")
        clear()
        if beli == "1":
            beli_pupuk0 = int(input("Jumlah pembelian pupuk organik (1 kg) - Rp. 10000: "))

            beli_pupuk += beli_pupuk0

            total_pupuk = beli_pupuk0 * 10000

            print(f"Total harga pupuk organik: Rp {total_pupuk}")
            lanjut = input("Tekan Enter untuk melanjutkan...")
            if lanjut == "":
                df = pd.read_csv('biaya_produksi.csv')
                df = pd.concat([df, pd.DataFrame([[tanggal_beli, 'Pupuk Organik (1 kg)', beli_pupuk0, 10000, total_pupuk]], columns=kolom)], ignore_index=True)
                df.to_csv('biaya_produksi.csv', index=False)
                clear()
                continue
        elif beli == "2":
            beli_benih_padi0 = int(input("Jumlah pembelian benih padi (1 kg) - Rp. 30000: "))
            
            beli_benih_padi += beli_benih_padi0

            total_benih_padi = beli_benih_padi0 * 30000

            print(f"Total harga benih padi: Rp {total_benih_padi}")
            lanjut = input("Tekan Enter untuk melanjutkan...")
            if lanjut == "":
                df = pd.read_csv('biaya_produksi.csv')
                df = pd.concat([df, pd.DataFrame([[tanggal_beli, 'Benih Padi (1 kg)', beli_benih_padi0, 30000, total_benih_padi]], columns=kolom)], ignore_index=True)
                df.to_csv('biaya_produksi.csv', index=False)
                clear()
                continue
        elif beli == "3":
            beli_benih_kacang0 = int(input("Jumlah pembelian benih Kacang (1 kg) - Rp. 30000: "))

            beli_benih_kacang += beli_benih_kacang0

            total_benih_kacang = beli_benih_kacang0 * 30000

            print(f"Total harga benih Kacang: Rp {total_benih_kacang}")
            lanjut = input("Tekan Enter untuk melanjutkan...")
            if lanjut == "":
                df = pd.read_csv('biaya_produksi.csv')
                df = pd.concat([df, pd.DataFrame([[tanggal_beli, 'Benih Kacang (1 kg)', beli_benih_kacang0, 30000, total_benih_kacang]], columns=kolom)], ignore_index=True)
                df.to_csv('biaya_produksi.csv', index=False)
                clear()
                continue
        elif beli == "4":
            beli_benih_jagung0 = int(input("Jumlah pembelian benih jagung (1 kg) - Rp. 45000: "))

            beli_benih_jagung += beli_benih_jagung0

            total_benih_jagung = beli_benih_jagung0 * 45000

            print(f"Total harga benih jagung: Rp {total_benih_jagung}")
            lanjut = input("Tekan Enter untuk melanjutkan...")
            if lanjut == "":
                df = pd.read_csv('biaya_produksi.csv')
                df = pd.concat([df, pd.DataFrame([[tanggal_beli, 'Benih Jagung (1 kg)', beli_benih_jagung0, 45000, total_benih_jagung]], columns=kolom)], ignore_index=True)
                df.to_csv('biaya_produksi.csv', index=False)
                clear()
                continue
        elif beli == "5":
            beli_pestisida0 = int(input("Jumlah pembelian pestisida (50 ml) - Rp. 25000: "))

            beli_pestisida += beli_pestisida0

            total_pestisida = beli_pestisida0 * 25000

            print(f"Total harga pestisida: Rp {total_pestisida}")
            lanjut = input("Tekan Enter untuk melanjutkan...")
            if lanjut == "":
                df = pd.read_csv('biaya_produksi.csv')
                df = pd.concat([df, pd.DataFrame([[tanggal_beli, 'Pestisida (50 ml)', beli_pestisida0, 25000, total_pestisida]], columns=kolom)], ignore_index=True)
                df.to_csv('biaya_produksi.csv', index=False)
                clear()
                continue
        elif beli == "6":
            break

    total_barang = beli_pupuk + beli_benih_padi + beli_benih_kacang + beli_benih_jagung + beli_pestisida
    total_harga = (beli_pupuk * 10000) + (beli_benih_padi * 30000) + (beli_benih_kacang * 30000) + (beli_benih_jagung * 45000) + (beli_pestisida * 25000)

    nama_w = 35
    jumlah_w = 5
    harga_w = 12

    print(f"{'=' * 30} Struk Pembelian {'=' * 30}")
    if beli_pupuk > 0:
        print(f"{'Pupuk Organik 1 kg (Rp. 10000)':<{nama_w}} x {beli_pupuk:>{jumlah_w}} = Rp. {beli_pupuk * 10000:>{harga_w}}")
    if beli_benih_padi > 0:
        print(f"{'Benih Padi 1 kg (Rp. 30000)':<{nama_w}} x {beli_benih_padi:>{jumlah_w}} = Rp. {beli_benih_padi * 30000:>{harga_w}}")
    if beli_benih_kacang > 0:
        print(f"{'Benih Kacang 1 kg (Rp. 30000)':<{nama_w}} x {beli_benih_kacang:>{jumlah_w}} = Rp. {beli_benih_kacang * 30000:>{harga_w}}")
    if beli_benih_jagung > 0:
        print(f"{'Benih Jagung 1 kg (Rp. 45000)':<{nama_w}} x {beli_benih_jagung:>{jumlah_w}} = Rp. {beli_benih_jagung * 45000:>{harga_w}}")
    if beli_pestisida > 0:
        print(f"{'Pestisida 50 ml (Rp. 25000)':<{nama_w}} x {beli_pestisida:>{jumlah_w}} = Rp. {beli_pestisida * 25000:>{harga_w}}")
    print(f"{'-' * 43} | {'-' * 16} +")
    print(f"Total Barang: {total_barang:>29} | Rp. {total_harga:>{harga_w}} | Total Harga")
    print("=" * 77)

    kolom_stok = ["Nama Barang", "Harga", "Jumlah Stok"]
    stok_awal = [["Pupuk Organik (1 kg)", 10000, 500],
                 ["Benih Padi (1 kg)", 30000, 500],
                 ["Benih Kacang (1 kg)", 30000, 500],
                 ["Benih Jagung (1 kg)", 45000, 500],
                 ["Pestisida (50 ml)", 25000, 300]]

    try:
       df = pd.read_csv('stok_barang.csv')
    except FileNotFoundError:
       df = pd.DataFrame(stok_awal, columns=kolom_stok)
       df.to_csv('stok_barang.csv', index=False)

    df = pd.read_csv('stok_barang.csv')
    df.loc[df['Nama Barang'] == 'Pupuk Organik (1 kg)', 'Jumlah Stok'] += beli_pupuk
    df.loc[df['Nama Barang'] == 'Benih Padi (1 kg)', 'Jumlah Stok'] += beli_benih_padi
    df.loc[df['Nama Barang'] == 'Benih Kacang (1 kg)', 'Jumlah Stok'] += beli_benih_kacang
    df.loc[df['Nama Barang'] == 'Benih Jagung (1 kg)', 'Jumlah Stok'] += beli_benih_jagung
    df.loc[df['Nama Barang'] == 'Pestisida (50 ml)', 'Jumlah Stok'] += beli_pestisida
    df.to_csv('stok_barang.csv', index=False)

    print("\nPembelian berhasil dicatat dan ditambahkan ke stok!")
    lanjut = input("\nTekan Enter untuk melanjutkan...")
    if lanjut == "":
        clear()

def aktivitas_harian(akun):
    clear()

    df = pd.read_csv('data_petugas.csv')

    ID = akun.iloc[0]["ID"]

    data = df[df["ID"] == ID].iloc[0]

    id_lahan = (data['ID Lahan'])

    kolom = ["ID", "Lahan", "Menyiram", "Memupuk", "Mengendalikan hama", "Tanggal"]

    try:
        df_aktivitas = pd.read_csv('aktivitas_harian.csv')
    except FileNotFoundError:
        df_aktivitas = pd.DataFrame(columns = kolom)
        df_aktivitas.to_csv('aktivitas_harian.csv', index=False)

    tanggal = datetime.now().strftime("%d-%m-%Y")

    data_hari_ini = df_aktivitas[(df_aktivitas["ID"] == ID) & 
                                 (df_aktivitas["Tanggal"] == tanggal)]
    
    if data_hari_ini.empty:
        aktivitas = {
            "ID": ID,
            "Lahan": id_lahan,
            "Menyiram": False,
            "Memupuk": False,
            "Mengendalikan hama": False,
            "Tanggal": tanggal
        }
        df_aktivitas = pd.concat([df_aktivitas, pd.DataFrame([aktivitas])], ignore_index=True)
        df_aktivitas.to_csv('aktivitas_harian.csv', index=False)
        
    while True:
        data_hari_ini = df_aktivitas[(df_aktivitas["ID"] == ID) & 
                                     (df_aktivitas["Tanggal"] == tanggal)]
        menyiram_done = data_hari_ini.iloc[0]["Menyiram"]
        memupuk_done = data_hari_ini.iloc[0]["Memupuk"]
        hama_done = data_hari_ini.iloc[0]["Mengendalikan hama"]

        print("\n===== Aktivitas Harian =====")
        print(f"Tanggal: {tanggal}")
        if menyiram_done and memupuk_done and hama_done:
            print("\nAnda sudah melakukan semua aktivitas pada hari ini!\n")
        print(f"1. Menyiram {'✔' if menyiram_done else '✘'}")
        print(f"2. Memupuk {'✔' if memupuk_done else '✘'}")
        print(f"3. mengendalikan hama {'✔' if hama_done else '✘'}")
        print("4. Kembali")

        input_aktivitas = input("Pilih Aktivitas yang sudah dilakukan: ")

        if input_aktivitas == "1":
            clear()
            if menyiram_done ==  True:
                print("Anda sudah melakukan aktivitas menyiram pada hari ini!")
                input("Tekan enter...")
                clear()
                continue
            menyiram_done = True
            df_aktivitas.loc[
                    (df_aktivitas["ID"] == ID) & (df_aktivitas["Tanggal"] == tanggal),
                    ["Menyiram"]
                    ] = [menyiram_done]
            df_aktivitas.to_csv('aktivitas_harian.csv', index=False)
        elif input_aktivitas == "2":
            clear()
            if memupuk_done ==  True:
                print("Anda sudah melakukan aktivitas memupuk pada hari ini!")
                input("Tekan enter...")
                clear()
                continue
            memupuk_done = True
            df_aktivitas.loc[
                    (df_aktivitas["ID"] == ID) & (df_aktivitas["Tanggal"] == tanggal),
                    ["Memupuk"]
                    ] = [memupuk_done]
            df_aktivitas.to_csv('aktivitas_harian.csv', index=False)
        elif input_aktivitas == "3":
            clear()
            if hama_done ==  True:
                print("Anda sudah melakukan aktivitas mengendalikan hama pada hari ini!")
                input("Tekan enter...")
                clear()
                continue
            hama_done = True
            df_aktivitas.loc[
                    (df_aktivitas["ID"] == ID) & (df_aktivitas["Tanggal"] == tanggal),
                    ["Mengendalikan hama"]
                    ] = [hama_done]
            df_aktivitas.to_csv('aktivitas_harian.csv', index=False)
        elif input_aktivitas == "4":
            break
        else:
            print("Pilihan tidak valid!")

    clear()

    print("Data aktivitas harian berhasil disimpan!")

def perkiraan():
    clear()

    while True:
        try:
            df = pd.read_csv('data_lahan.csv')
        except Exception:
            print("Data lahan belum ada")
            input("Tekan enter untuk melanjutkan...")
            clear()
            break
    
        print("===== PERKIRAAN HASIL PANEN DAN KEUNTUNGAN =====")
        print("1. Lahan 1")
        print("2. Lahan 2")
        print("3. Lahan 3")
        print("4. Kembali")

        pilih_lahan = input("Pilih Lahan atau kembali: ")

        if pilih_lahan == "1":
            clear() 
            data_filter = df[df["ID Lahan"] == 1]
            if data_filter.empty:
                print("Data lahan belum ada")
                input("Tekan enter untuk melanjutkan...")
                clear()
                continue
            else:
                data = df[df["ID Lahan"] == 1].iloc[0]
                print("===== PERKIRAAN HASIL PANEN DAN KEUNTUNGAN =====")
                print(f"Tanaman                 : {data["Nama Tanaman"]:>22}")
                print(f"Tangga tanam            : {data["Tanggal Tanam"]:>22}")
                print(f"Perkiraan tanggal panen : {data["Perkiraan Panen"]:>22}")
                print(f"Perkiraan hasil panen   : {'5000 kg' if data['Nama Tanaman'] == "Padi" else '6000 kg' if data['Nama Tanaman'] == "Jagung" else "2000 kg":>22}")
                print(f"Perkiraan hasil jual    : {'Rp. 20000000' if data['Nama Tanaman'] == "Padi" else 'Rp. 18000000' if data['Nama Tanaman'] == "Jagung" else "Rp. 16000000":>22}")
                print(f"Biaya produksi          : {'Rp. 8000000' if data['Nama Tanaman'] == "Padi" else 'Rp. 6000000' if data['Nama Tanaman'] == "Jagung" else "Rp. 6000000":>22}")
                print(f"Perkiraan keuntungan    : {'Rp. 12000000' if data['Nama Tanaman'] == "Padi" else 'Rp. 12000000' if data['Nama Tanaman'] == "Jagung" else "Rp. 10000000":>22}")
                input("\nTekan enter untuk kembali...")
                clear()
        elif pilih_lahan == "2":
            clear()
            data_filter = df[df["ID Lahan"] == 2]
            if data_filter.empty:
                print("Data lahan belum ada")
                input("Tekan enter untuk melanjutkan...")
                clear()
            else:
                data = df[df["ID Lahan"] == 2].iloc[0]
                print("===== PERKIRAAN HASIL PANEN DAN KEUNTUNGAN =====")
                print(f"Tanaman                 : {data["Nama Tanaman"]:>22}")
                print(f"Tangga tanam            : {data["Tanggal Tanam"]:>22}")
                print(f"Perkiraan tanggal panen : {data["Perkiraan Panen"]:>22}")
                print(f"Perkiraan hasil panen   : {'5000 kg' if data['Nama Tanaman'] == "Padi" else '6000 kg' if data['Nama Tanaman'] == "Jagung" else "2000 kg":>22}")
                print(f"Perkiraan hasil jual    : {'Rp. 20000000' if data['Nama Tanaman'] == "Padi" else 'Rp. 18000000' if data['Nama Tanaman'] == "Jagung" else "Rp. 16000000":>22}")
                print(f"Biaya produksi          : {'Rp. 8000000' if data['Nama Tanaman'] == "Padi" else 'Rp. 6000000' if data['Nama Tanaman'] == "Jagung" else "Rp. 6000000":>22}")
                print(f"Perkiraan keuntungan    : {'Rp. 12000000' if data['Nama Tanaman'] == "Padi" else 'Rp. 12000000' if data['Nama Tanaman'] == "Jagung" else "Rp. 10000000":>22}")
                input("\nTekan enter untuk kembali...")
                clear()
        elif pilih_lahan == "3":
            clear()
            data_filter = df[df["ID Lahan"] == 3]
            if data_filter.empty:
                print("Data lahan belum ada")
                input("Tekan enter untuk melanjutkan...")
                clear()
            else:
                data = df[df["ID Lahan"] == 3].iloc[0]
                print("===== PERKIRAAN HASIL PANEN DAN KEUNTUNGAN =====")
                print(f"Tanaman                 : {data["Nama Tanaman"]:>22}")
                print(f"Tangga tanam            : {data["Tanggal Tanam"]:>22}")
                print(f"Perkiraan tanggal panen : {data["Perkiraan Panen"]:>22}")
                print(f"Perkiraan hasil panen   : {'5000 kg' if data['Nama Tanaman'] == "Padi" else '6000 kg' if data['Nama Tanaman'] == "Jagung" else "2000 kg":>22}")
                print(f"Perkiraan hasil jual    : {'Rp. 20000000' if data['Nama Tanaman'] == "Padi" else 'Rp. 18000000' if data['Nama Tanaman'] == "Jagung" else "Rp. 16000000":>22}")
                print(f"Biaya produksi          : {'Rp. 8000000' if data['Nama Tanaman'] == "Padi" else 'Rp. 6000000' if data['Nama Tanaman'] == "Jagung" else "Rp. 6000000":>22}")
                print(f"Perkiraan keuntungan    : {'Rp. 12000000' if data['Nama Tanaman'] == "Padi" else 'Rp. 12000000' if data['Nama Tanaman'] == "Jagung" else "Rp. 10000000":>22}")
                input("\nTekan enter untuk kembali...")
                clear()
        elif pilih_lahan == "4":
            clear()
            break
        else:
            print("\nPilihan tidak valid\n")
            clear()

def laporan_pekerja():
    kolom = ["ID", "Username", "Password", "Nama Lengkap", "No. Telepon", "Alamat"]

    try:
        df = pd.read_csv('data_petugas.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=kolom)
        df.to_csv('data_petugas.csv', index=False)

    df = pd.read_csv('data_petugas.csv')

    try:
        df_aktivitas = pd.read_csv('aktivitas_harian.csv')
    except FileNotFoundError:
        df_aktivitas = pd.DataFrame(columns=["ID", "Lahan" "Menyiram", "Memupuk", "Mengendalikan hama", "Tanggal"])
        df_aktivitas.to_csv('aktivitas_harian.csv', index=False)

    df_aktivitas = pd.read_csv('aktivitas_harian.csv')

    while True:
        print("\n=== Daftar Pekerja ===")
        if df.empty:
            print("Belum ada data pekerja.")
        else:
            print(tabulate(df.loc[:, ["ID", "Nama Lengkap"]], headers=["ID", "Nama Lengkap"], tablefmt='fancy_grid', showindex=False))

        tanggal = datetime.now().strftime("%d-%m-%Y")
        
        pilih_petugas = (input('Pilih ID Petugas (Ketik "q" untuk kembali): '))

        if pilih_petugas == "q":
            clear()
            break

        if not pilih_petugas.isdigit():
            print("\nID harus berupa angka!")
            input("Tekan enter untuk melanjutkan...")
            continue

        pilih_petugas = int(pilih_petugas)

        if pilih_petugas not in df["ID"].astype(int).values:
            clear()
            print("ID tidak ditemukan di data pekerja!")
            input("Tekan enter untuk melanjutkan...")
            clear()
            continue

        data_aktivitas = df_aktivitas[(df_aktivitas["ID"].astype(int) == pilih_petugas) &
                                      (df_aktivitas["Tanggal"] == tanggal)]
        
        data = df[df["ID"].astype(int) == pilih_petugas].iloc[0]

        if data_aktivitas.empty:
            clear()
            print(f"===== LAPORAN PETUGAS {data["Nama Lengkap"]} =====")
            print(f"Tanggal : {tanggal:>20}")
            print(f"Nama    : {data['Nama Lengkap']:>20}")
            print(f"Lahan   : {f"Lahan {data['ID Lahan']}":>20}")
            print(f"Menyiram {'✘':>21}")
            print(f"Memupuk {'✘':>22}")
            print(f"Mengendalikan hama {'✘':>11}")
            input("\nTekan enter untuk kembali...")
            clear()
            continue

        menyiram_done = data_aktivitas.iloc[0]["Menyiram"]
        memupuk_done = data_aktivitas.iloc[0]["Memupuk"]
        hama_done = data_aktivitas.iloc[0]["Mengendalikan hama"]

        clear()

        print(f"===== LAPORAN PETUGAS {data["Nama Lengkap"]} =====")
        print(f"Tanggal : {tanggal:>20}")
        print(f"Nama    : {data['Nama Lengkap']:>20}")
        print(f"Lahan   : {f"Lahan {data['ID Lahan']}":>20}")
        print(f"Menyiram {'✔' if menyiram_done else '✘':>21}")
        print(f"Memupuk {'✔' if memupuk_done else '✘':>22}")
        print(f"Mengendalikan hama {'✔' if hama_done else '✘':>11}")
        input("\nTekan enter untuk kembali...")
        clear()

def laporan_lahan():
    while True:
        clear()

        try:
            df_lahan = pd.read_csv("data_lahan.csv")
        except FileNotFoundError:
            clear()
            print("Data lahan belum ada!")
            input("Tekan enter untuk kembali...")
            clear()
            break

        try:
            df_aktivitas = pd.read_csv("aktivitas_harian.csv")
        except FileNotFoundError:
            clear()
            print("Data aktivitas belum ada!")
            input("Tekan enter untuk kembali...")
            clear()
            break

        tanggal = datetime.now().strftime("%d-%m-%Y")

        print("\n=== Daftar Lahan ===")
        print(tabulate(df_lahan[["ID Lahan", "Nama Tanaman"]], headers=["ID Lahan", "Nama Tanaman"], tablefmt="fancy_grid", showindex=False))

        pilih = input('Pilih ID Lahan (ketik "q" untuk kembali): ')

        if pilih.lower() == "q":
            clear()
            break

        if not pilih.isdigit():
            print("Input harus angka!")
            input("Tekan enter untuk melanjutkan...")
            continue

        pilih = int(pilih)

        if pilih not in df_lahan["ID Lahan"].astype(int).values:
            clear()
            print("ID Lahan tidak ditemukan!")
            input("Tekan enter...")
            continue

        data_lahan = df_lahan[df_lahan["ID Lahan"] == pilih].iloc[0]

        data_aktivitas = df_aktivitas[
            (df_aktivitas["Lahan"] == pilih) &
            (df_aktivitas["Tanggal"] == tanggal)
        ]

        if data_aktivitas.empty:
            menyiram_done = False
            memupuk_done = False
            hama_done = False
        else:
            menyiram_done = data_aktivitas["Menyiram"].any()
            memupuk_done = data_aktivitas["Memupuk"].any()
            hama_done = data_aktivitas["Mengendalikan hama"].any()

        clear()
        print(f"===== LAPORAN LAHAN {data_lahan['ID Lahan']} =====")
        print(f"Tanggal         : {tanggal:>20}")
        print(f"Nama Tanaman    : {data_lahan['Nama Tanaman']:>20}")
        print(f"Luas Lahan      : {f"{data_lahan['Luas Lahan (ha)']} ha":>20}")
        print(f"Tanggal Tanam   : {data_lahan['Tanggal Tanam']:>20}")
        print(f"Perkiraan panen : {data_lahan['Perkiraan Panen']:>20}")
        print(f"Disiram {'✔' if menyiram_done else '✘':>29}")
        print(f"Dipupuk {'✔' if memupuk_done else '✘':>30}")
        print(f"Pengendalian hama {'✔' if hama_done else '✘':>19}")

        input("\nTekan enter untuk kembali...")


def stok():
    clear()
    kolom = ["Nama Barang", "Harga", "Jumlah Stok"]
    stok_awal = [["Pupuk Organik (1 kg)", 10000, 500],
                 ["Benih Padi (1 kg)", 30000, 500],
                 ["Benih Kacang (1 kg)", 30000, 500],
                 ["Benih Jagung (1 kg)", 45000, 500],
                 ["Pestisida (50 ml)", 25000, 300]]

    try:
       df = pd.read_csv('stok_barang.csv')
    except FileNotFoundError:
       df = pd.DataFrame(stok_awal, columns=kolom)
       df.to_csv('stok_barang.csv', index=False)

    df = pd.read_csv('stok_barang.csv')

    print("\n================== Stok Barang ==================")
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

    input("\nTekan enter untuk melanjutkan...")
    clear()

def data_lahan(akun):
    df = pd.read_csv('data_petugas.csv')

    ID = akun.iloc[0]["ID"]

    id_lahan_petugas = akun.iloc[0]["ID Lahan"]

    data = df[df["ID"] == ID].iloc[0]

    file = "data_lahan.csv"
    kolom = ["ID Lahan", "Nama Tanaman", "Luas Lahan (ha)", "Tanggal Tanam", "Perkiraan Panen"]

    try:
       df_lahan = pd.read_csv('data_lahan.csv')
    except Exception:
       df_lahan = pd.DataFrame(columns=kolom)
       df_lahan.to_csv('data_lahan.csv', index=False)

    if id_lahan_petugas in df_lahan["ID Lahan"].values:
        print("\nLahan anda sudah ditanam!")
        input("Tekan enter untuk kembali...")
        clear()
        return
   
    print(f"\n=== Lahan anda (Lahan {int(data['ID Lahan'])}) ===")
    print("1. Padi")
    print("2. Jagung")
    print("3. Kacang")
    tanaman = input("Masukkan lahan yang ingin ditanam: ")
    if tanaman == "1":
        nama = "Padi"
        df_lahan = pd.read_csv('stok_barang.csv')
        id = data['ID Lahan']
        df_lahan.loc[df_lahan['Nama Barang'] == 'Benih Padi (1 kg)', 'Jumlah Stok'] -= 200
        df_lahan.loc[df_lahan['Nama Barang'] == 'Pupuk Organik (1 kg)', 'Jumlah Stok'] -= 100
        df_lahan.loc[df_lahan['Nama Barang'] == 'Pestisida (50 ml)', 'Jumlah Stok'] -= 20
        df_lahan.to_csv('stok_barang.csv', index=False)
    elif tanaman == "2":
        nama = "Jagung"
        id = data['ID Lahan']
        df_lahan = pd.read_csv('stok_barang.csv')
        df_lahan.loc[df_lahan['Nama Barang'] == 'Benih Jagung (1 kg)', 'Jumlah Stok'] -= 40
        df_lahan.loc[df_lahan['Nama Barang'] == 'Pupuk Organik (1 kg)', 'Jumlah Stok'] -= 100
        df_lahan.loc[df_lahan['Nama Barang'] == 'Pestisida (50 ml)', 'Jumlah Stok'] -= 20
        df_lahan.to_csv('stok_barang.csv', index=False)
    elif tanaman == "3":
        nama = "Kacang"
        id = data['ID Lahan']
        df_lahan = pd.read_csv('stok_barang.csv')
        df_lahan.loc[df_lahan['Nama Barang'] == 'Benih Kacang (1 kg)', 'Jumlah Stok'] -= 100
        df_lahan.loc[df_lahan['Nama Barang'] == 'Pupuk Organik (1 kg)', 'Jumlah Stok'] -= 100
        df_lahan.loc[df_lahan['Nama Barang'] == 'Pestisida (50 ml)', 'Jumlah Stok'] -= 20
        df_lahan.to_csv('stok_barang.csv', index=False)
    else:
        print("Pilihan tidak tersedia.")
        return
    luas = 1
    tanam = datetime.now().strftime("%d-%m-%Y")
    tanggal_tanam = datetime.strptime(tanam, "%d-%m-%Y")
    tanggal_panen = tanggal_tanam + timedelta(days=90)
    panen= tanggal_panen.strftime("%d-%m-%Y")
    
    print(f"Tanggal tanam {nama}: {tanam}")
    print(f"Perkiraan Panen untuk {nama}: {panen}")

    df_lahan = pd.read_csv(file)
    df_lahan = pd.concat([df_lahan, pd.DataFrame([[id, nama, luas, tanam, panen]], columns=kolom)], ignore_index=True)
    df_lahan.to_csv(file, index=False)

    lanjut = input("Tekan enter untuk melanjutkkan...")

    clear()

    print("Data tanaman berhasil disimpan!")

def laporan_pribadi(akun):
    clear()
    df = pd.read_csv('data_petugas.csv')

    ID = akun.iloc[0]["ID"]

    data = df[df["ID"] == ID].iloc[0]

    tanggal = datetime.now().strftime("%d-%m-%Y")

    df_aktivitas = pd.read_csv('aktivitas_harian.csv')

    data_aktivitas = df_aktivitas[(df_aktivitas["ID"] == ID) & 
                                  (df_aktivitas["Tanggal"] == tanggal)]
    
    menyiram_done = data_aktivitas.iloc[0]["Menyiram"]
    memupuk_done = data_aktivitas.iloc[0]["Memupuk"]
    hama_done = data_aktivitas.iloc[0]["Mengendalikan hama"]

    print("========== LAPORAN PRIBADI ==========")
    print(f"Tanggal : {tanggal:>20}")
    print(f"Nama    : {data['Nama Lengkap']:>20}")
    print(f"Lahan   : {f"Lahan {data['ID Lahan']}":>20}")
    print(f"Menyiram {'✔' if menyiram_done else '✘':>21}")
    print(f"Memupuk {'✔' if memupuk_done else '✘':>22}")
    print(f"Mengendalikan hama {'✔' if hama_done else '✘':>11}")
    input("\nTekan enter untuk kembali...")
    clear()


def profil_pekerja(akun):
    clear()
    df = pd.read_csv('data_petugas.csv')

    ID = akun.iloc[0]["ID"]

    while True:
        data = df[df["ID"] == ID].iloc[0]
        print("\n========== Profil Saya ==========")
        print(f"ID            : {data['ID']}")
        print(f"Username      : {data['Username']}")
        print(f"Password      : {data['Password']}")
        print(f"Nama Lengkap  : {data['Nama Lengkap']}")
        print(f"No. Telepon   : {data['No. Telepon']}")
        print(f"Alamat        : {data['Alamat']}")
        print("\n1. Edit Profil")
        print("2. Kembali")

        pilih = input("Masukkan pilihan: ")

        if pilih == "1":
            clear()
            while True:
                data = df[df["ID"] == ID].iloc[0]
                print("\n========== Edit Profil ==========")
                print(f"1. Username      : {data['Username']}")
                print(f"2. Password      : {data['Password']}")
                print(f"3. Nama Lengkap  : {data['Nama Lengkap']}")
                print(f"4. No. Telepon   : {data['No. Telepon']}")
                print(f"5. Alamat        : {data['Alamat']}")
                print("6. Kembali")
                sub_pilihan = input("\nPilih data yang ingin diubah: ")

                if sub_pilihan == "1":
                    new_username = input("\nUsername baru: ")
                    df.loc[df['ID'] == id, 'Username'] = new_username
                    df.to_csv('data_petugas.csv', index=False)
                    clear()
                    print("Data berhasil diubah!")
                elif sub_pilihan == "2":
                    new_password = input("\nPassword baru: ")
                    df.loc[df['ID'] == id, 'Password'] = new_password
                    df.to_csv('data_petugas.csv', index=False)
                    clear()
                    print("Data berhasil diubah!")
                elif sub_pilihan == "3":
                    new_nama     = input("\nNama lengkap baru: ")
                    df.loc[df['ID'] == id, 'Nama Lengkap'] = new_nama
                    df.to_csv('data_petugas.csv', index=False)
                    clear()
                    print("Data berhasil diubah!")
                elif sub_pilihan == "4":
                    while True:
                        try:
                            new_telp = int(input("\nNo. telepon baru: "))
                            break
                        except Exception:
                            print("\nNo. telepon harus berupa angka!")
                            continue
                    df.loc[df['ID'] == id, 'No. Telepon'] = new_telp
                    df.to_csv('data_petugas.csv', index=False)
                    clear()
                    print("Data berhasil diubah!")
                elif sub_pilihan == "5":
                    new_alamat   = input("\nAlamat baru: ")
                    df.loc[df['ID'] == id, 'Alamat'] = new_alamat
                    df.to_csv('data_petugas.csv', index=False)
                    clear()
                    print("Data berhasil diubah!")
                elif sub_pilihan == "6":
                    break
                else:
                    print("Pilihan tidak valid!")
                    continue

            df.to_csv('data_petugas.csv', index=False)

            clear()

            print("\nProfil berhasil diperbarui!\n")

            data = df[df["ID"] == ID].iloc[0]

        elif pilih == "2":
            clear()
            break
        else:
            print("Pilihan tidak valid!")


def main():
    loading()
    while True:
        splash_farmify()
        print("\n====== MENU LOGIN ======")
        print("1. Masuk sebagai Admin")
        print("2. Masuk sebagai Petugas")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            pw = input("Masukkan password admin: ")
            clear()
            if pw == PassAdmin:
                while True:
                    print("\nSelamat datang, Admin!")
                    print("============== Menu Admin ==============")
                    print("1. Kelola Pekerja")
                    print("2. Biaya Produksi")
                    print("3. Perkiraan Hasil Panen dan Keuntungan")
                    print("4. Laporan")
                    print("5. Logout")

                    pilihan_admin = input("Masukkan pilihan: ")
                    clear()
                    if pilihan_admin == "1":
                        while True:
                            kolom = ["ID", "Username", "Password", "Nama Lengkap", "No. Telepon", "Alamat"]

                            try:
                                df = pd.read_csv('data_petugas.csv')
                            except FileNotFoundError:
                                df = pd.DataFrame(columns=kolom)
                                df.to_csv('data_petugas.csv', index=False)

                            df = pd.read_csv('data_petugas.csv')
                            print("\n=== Daftar Pekerja ===")
                            if df.empty:
                                print("Belum ada data pekerja.")
                            else:
                                print(tabulate(df.loc[:, ["ID", "Nama Lengkap"]], headers=["ID", "Nama Lengkap"], tablefmt='fancy_grid', showindex=False))
                            print("1. Tambah Pekerja")
                            print("2. Update data Pekerja")
                            print("3. Hapus Pekerja")
                            print("4. Kembali")
                        
                            sub_pilihan = input("Masukkan pilihan: ")
                            clear()
                            if sub_pilihan == "1":
                                Tambah_pekerja()
                                print("Pekerja baru berhasil ditambahkan!")
                                clear()
                            elif sub_pilihan == "2":
                                update_petugas()
                            elif sub_pilihan == "3":
                                hapus_petugas()
                                clear()
                            elif sub_pilihan == "4":
                                break
                            else:
                                print("\nPilihan tidak tersedia.")
                    elif pilihan_admin == "2":
                        biaya_produksi()
                        print("Biaya produksi berhasil dicatat dan ditambahkan ke stok!")
                        clear()
                    elif pilihan_admin == "3":
                        perkiraan()
                    elif pilihan_admin == "4":
                        while True:
                            print("=========== Menu Laporan ===========")
                            print("1. Laporan Aktivitas Harian Petugas")
                            print("2. Laporan Lahan")
                            print("3. Kembali")

                            pilih_laporan = input("Pilih Laporan: ")

                            if pilih_laporan == "1":
                                clear()
                                laporan_pekerja()
                            elif pilih_laporan == "2":
                                clear()
                                laporan_lahan()
                            elif pilih_laporan == "3":
                                clear()
                                break
                            else:
                                print("Pilihan tidak valid")
                    elif pilihan_admin == "5":
                        clear()
                        break
                    else:
                        print("\nPilihan tidak tersedia.")
            else:
                print("\nPassword salah!")

        elif pilihan == "2":
            user = input("\nMasukkan username: ")
            pwpetugas = input("Masukkan password: ")

            df = pd.read_csv('data_petugas.csv')

            akun = df[(df["Username"] == user) & (df["Password"] == pwpetugas)]

            clear()

            if not akun.empty:
                nama_petugas = akun.iloc[0]["Nama Lengkap"]
                while True:
                    print(f"\nSelamat datang, {nama_petugas}!")
                    print("1. Tanam Lahan")
                    print("2. Catat Aktivitas Harian")
                    print("3. Stok Barang")
                    print("4. Laporan Pribadi")
                    print("5. Lihat dan edit Profil")
                    print("6. Logout")

                    pilihan_petugas = input("Masukkan pilihan: ")
                    if pilihan_petugas == "1":
                        data_lahan(akun)
                    elif pilihan_petugas == "2":
                        aktivitas_harian(akun)
                    elif pilihan_petugas == "3":
                        stok()
                    elif pilihan_petugas == "4":
                        laporan_pribadi(akun)
                    elif pilihan_petugas == "5":
                        profil_pekerja(akun)
                    elif pilihan_petugas == "6":
                        clear()
                        break
                    else:
                        clear()
                        print("\nPilihan tidak tersedia.")
            else:
                print("\nUsername atau password salah!")

        elif pilihan == "3":
            clear()
            print("Telah Keluar dari program.")
            break
        else:
            print("\nPilihan tidak tersedia.")

main()