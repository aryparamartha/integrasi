import pymysql
import time

def new_delete(con_toko, con_clone):
    cur_toko = con_toko.cursor()
    cur_clone = con_clone.cursor()

    cur_toko.execute("select count(id_transaksi) from tb_transaksi")
    global totaldata
    totaldata = cur_toko.fetchone()

    cur_clone.execute("select count(id_transaksi) from tb_transaksi")
    global totaldataclone
    totaldataclone = cur_clone.fetchone()

    cur_toko.execute("select id_transaksi from tb_transaksi")
    idtoko = cur_toko.fetchall()
    # print("id toko: %d" %(idtoko[1][0]))

    sql = ("select count(id_transaksi) from tb_transaksi")
    cur_toko.execute(sql)
    cur_clone.execute(sql)

    jumdata = cur_toko.fetchone()
    jumclone = cur_clone.fetchone()

    cur_clone.execute("select id_transaksi from tb_transaksi")
    idclone = cur_clone.fetchall()
    #print("id clone %d" %(idclone[1][0]))

    cur_clone.execute("SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_toko_clone' AND   TABLE_NAME   = 'tb_transaksi'")
    totalincclone = cur_clone.fetchone()

    cur_toko.execute("SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_toko_ol' AND   TABLE_NAME   = 'tb_transaksi'")
    totalinc = cur_toko.fetchone()

    i=0
    for i in range(0, totalinc[0]):
        if jumdata[0]!=jumclone[0]:
            if idtoko[i][0]>idclone[i][0]:
                print("delete sedang berlangsung")
                cur_clone.execute("delete from tb_transaksi where id_transaksi=%d" %(idclone[i][0]))
                con_clone.commit()
                break