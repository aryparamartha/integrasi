import pymysql
import time

waktu = time.time()
con_toko = pymysql.connect(host="localhost", user="root", password="", database="db_toko_ol")
cur_toko = con_toko.cursor()

con_clone = pymysql.connect(host="localhost", user="root", password="", database="db_toko_clone")
cur_clone = con_clone.cursor()

try:
    print("1. Input data baru")
    print("2. Update data")
    pilihan = int(input("Masukkan Pilihan Menu  :"))

    if pilihan==1:
        idpelanggan = int(input("Masukkan ID Pelanggan  :"))
        no_rek = int(input("Masukkan No Rek Pelanggan   :"))
        totaltrans = int(input("Masukkan Total Belanja      :"))

        cur_toko.execute("INSERT INTO tb_transaksi (id_pelanggan, no_rek, total_trans, status_lunas, created_at, updated_at) VALUES(%d, '%d', '%d', 0, %d, %d)" %(idpelanggan, no_rek, totaltrans, waktu, waktu))
        con_toko.commit()

        print("Input Data Berhasil!")

    elif pilihan==2:
        bank = int(input("Tekan 1 jika input data bank tekan asal jika tidak:"))
        if bank == 1:
            idtransaksi = int(input("Masukkan ID transaksi yg ingin di ubah :"))
            status = int(input("Masukkan Status Baru    :"))

            cur_clone.execute("update tb_transaksi set status_lunas=%d, updated_at=%d where id_transaksi=%d" %(status, waktu, idtransaksi))
            con_clone.commit()
        else:
            idtransaksi = int(input("Masukkan ID transaksi yg ingin di ubah:    "))
            no_rek = int(input("Masukkan No Rek baru    :"))
            totaltrans = int(input("Masukkan total trans baru   :"))

            cur_toko.execute("update tb_transaksi set no_rek=%d, total_trans=%d, updated_at=%d where id_transaksi=%d" %(no_rek, totaltrans, waktu, idtransaksi))
            con_toko.commit()

except:
    print("Koneksi gagal!")