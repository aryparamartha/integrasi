import pymysql
import time
import json

from insert import new_insert
from delete import new_delete
from update import new_update

delay = int(input("Masukkan delay   :"))
i = 1
while True:
    con_toko = pymysql.connect(host="localhost", user="root", password="", database="db_toko")
    con_clone = pymysql.connect(host="localhost", user="root", password="", database="db_bank")

    i=i+1
    #insert
    new_insert(con_toko, con_clone)

    #delete
    new_delete(con_toko, con_clone)

    #update
    new_update(con_toko, con_clone)

    time.sleep(delay)
