import pymysql
import time
import json

from jason import tokoInsertJSON

def new_insert(con_toko, con_clone):

    waktu = time.time()
    cur_toko = con_toko.cursor()
    cur_clone = con_clone.cursor()

    cur_toko.execute("SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_toko' AND   TABLE_NAME   = 'tb_transaksi'")
    global totalinc
    totalinc = cur_toko.fetchone()

    cur_clone.execute("SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_bank' AND   TABLE_NAME   = 'tb_transaksi'")
    global totalincclone
    totalincclone = cur_clone.fetchone()

    if totalinc[0] != totalincclone[0]:
        print("ada insert")
        if totalinc[0] > totalincclone[0]:
            print("insert dari host 1")
            with open("toko.json", "r", encoding='utf-8') as outfile:
                try:
                    listdata = json.load(outfile)
                except:
                    listdata = []
            for i in range(totalincclone[0], totalinc[0]):
                cur_toko.execute("select id_transaksi, id_pelanggan, no_rek, total_trans, created_at, updated_at from tb_transaksi where id_transaksi=%i" % i)
                insertoko = cur_toko.fetchone()
                id_transaksi = insertoko[0]
                id_pelanggan = insertoko[1]
                no_rek = insertoko[2]
                total_trans = insertoko[3]
                create = insertoko[4]
                update = insertoko[5]
                con_toko.commit()
                insert = True
                for row in listdata:
                    if(id_transaksi == row['id_transaksi'] and row['status']=='insert'):
                        insert = False
                        break
                if(insert==True):
                    tokoInsertJSON(id_transaksi, id_pelanggan, no_rek, total_trans, create, update)
            openfile = open("toko.json", "r")
            listdata = json.load(openfile)

            for json_toko in listdata:
                if json_toko['status'] == 'insert' and json_toko['sync'] == True:
                    id_transaksi, id_pelanggan, no_rek, total_trans, created_at, updated_at = json_toko['id_transaksi'], json_toko['id_pelanggan'], \
                                                                                      json_toko['no_rek'], json_toko['total_trans'], json_toko['created_at'], json_toko['updated_at']
                    cur_clone.execute("insert into tb_transaksi(id_transaksi, id_pelanggan, no_rek, total_trans, created_at, updated_at) values(%s, %s, %s, %s, %s, %s)"
                                      %(id_transaksi, id_pelanggan, no_rek, total_trans, created_at, updated_at))
                    con_clone.commit()
                    
                    openfile2 = open("toko.json", "r+")
                    listdata2 = json.load(openfile2)
                    for row in listdata2:
                        row['sync'] = False
                        openfile2.seek(0)
                        json.dump(listdata2, openfile2, indent=4)
                        openfile2.truncate()
        #         cur_clone.execute("insert into tb_transaksi values(%d, %d, %d, %d, default, %d, %d)" %(id_transaksi, id_pelanggan, no_rek, total_trans, create, update))
        #         con_clone.commit()
        #
        # elif totalincclone[0] > totalinc[0]:
        #     print("insert dari host 2")
        #     for i in range(totalinc[0], totalincclone[0]):
        #         cur_clone.execute("select id_transaksi, id_pelanggan, no_rek, total_trans, created_at, updated_at from tb_transaksi where id_transaksi=%i" % i)
        #         insertclone = cur_clone.fetchone()
        #         id_transaksi = insertclone[0]
        #         id_pelanggan = insertclone[1]
        #         no_rek = insertclone[2]
        #         total_trans = insertclone[3]
        #         create = insertclone[4]
        #         update = insertclone[5]
        #         con_clone.commit()
        #         cur_toko.execute("insert into tb_transaksi values(%d, %d, %d, %d, default, %d, %d)" %(id_transaksi, id_pelanggan, no_rek, total_trans, create, update))
        #         con_toko.commit()
        #
        #
        #
        #
