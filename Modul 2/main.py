import pymysql
import time
import json

from insert import new_insert
from delete import new_delete
from update import new_update

delay = int(input("Masukkan delay   :"))
i = 0
with open("toko.json", "w", encoding='utf-8') as outfile:
    try:
        data = json.load(outfile)
    except:
        data = []

with open("bank.json", "w", encoding='utf-8') as outfile:
    try:
        data = json.load(outfile)
    except:
        data = []
while True:
    con_toko = pymysql.connect(host="localhost", user="root", password="", database="db_toko")
    con_clone = pymysql.connect(host="localhost", user="root", password="", database="db_bank")

    i=i+1
    #insert
    new_insert(con_toko, con_clone)

    # #delete
    # new_delete(con_toko, con_clone)
    #
    # #update
    # new_update(con_toko, con_clone)

    time.sleep(delay)
