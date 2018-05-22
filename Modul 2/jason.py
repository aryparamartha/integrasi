import json

def tokoInsertJSON(id_transaksi, id_pelanggan, no_rek, total_trans, created_at, updated_at):
    with open("toko.json", "r", encoding='utf-8') as outfile:
        try:
            listdata = json.load(outfile)
        except:
            listdata = []
    json_toko = {'id_transaksi': id_transaksi, 'id_pelanggan': id_pelanggan, 'no_rek': no_rek,
                 'total_trans': total_trans, 'created_at': str(created_at), 'updated_at': str(updated_at), 'status': 'insert', 'sync': True}
    listdata.append(json_toko)
    with open("toko.json", "r+", encoding='utf-8') as outfile:
        json.dump(listdata, outfile, indent=4)

def tokoUpdateJSON(id_transaksi, id_pelanggan, no_rek, total_trans, updated_at):
    with open("toko.json", "r", encoding='utf-8') as outfile:
        try:
            listdata = json.load(outfile)
        except:
            listdata = []
    json_toko = {'id_transaksi': id_transaksi, 'id_pelanggan': id_pelanggan, 'no_rek': no_rek,
                 'total_trans': total_trans, 'updated_at': str(updated_at), 'status': 'update', 'sync': True}
    listdata.append(json_toko)
    with open("toko.json", "r+", encoding='utf-8') as outfile:
        json.dump(listdata, outfile, indent=4)

def tokoDeleteJSON(id_transaksi):
    with open("toko.json", "r", encoding='utf-8') as outfile:
        try:
            listdata = json.load(outfile)
        except:
            listdata = []
    json_toko = {'id_transaksi': id_transaksi, 'status': 'delete', 'sync': True}
    listdata.append(json_toko)
    with open("toko.json", "w", encoding='utf-8') as outfile:
        json.dump(listdata, outfile, indent=4)

def bankUpdateJSON(id_transaksi, status_lunas, updated_at):
    with open("bank.json", "r", encoding='utf-8') as outfile:
        try:
            listdata = json.load(outfile)
        except:
            listdata = []
    json_bank = {'id_transaksi': id_transaksi, 'status_lunas': status_lunas, 'updated_at': updated_at,'status': 'update', 'sync': True}
    listdata.append(json_bank)
    with open("bank.json", "w", encoding='utf-8') as outfile:
        json.dump(listdata, outfile, indent=4)