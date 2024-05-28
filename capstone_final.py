user_login = {}

def main():
    stok = [
        {
            "id": "123MN",
            "nama_barang": "Laptop",
            "kategori": {
                "id": "1",
                "nama": "Elektronik"
            },
            "vendor": "Vendor A",
            'gudang' : {
                "id" : "1",
                "nama" : "Gudang 1",
                "lokasi" : "Jakarta"
            },
            'stok' : 0,
            'transaction' : [],
            'input_by' : {
                'id' : "1ABCDEF",
                'name' : "John"
            },
            'update_by' : {
                'id' : "1ABCDEF",
                'name' : "John"
            },
        },
    ]
    
    master_kategori = [
        {
            "id": "1",
            "nama": "Elektronik"
        },
        {
            "id": "2",
            "nama": "Pakaian"
        },
        {
            "id": "3",
            "nama": "Makanan"
        },
        {
            "id": "4",
            "nama": "Minuman"
        },
        {
            "id": "5",
            "nama": "Alat Tulis"
        }
    ]
    master_gudang = [
        {
            "id": "1",
            "nama": "Gudang 1",
            "lokasi": "Jakarta"
        },
        {
            "id": "2",
            "nama": "Gudang 2",
            "lokasi": "Surabaya"
        },
        {
            "id": "3",
            "nama": "Gudang 3",
            "lokasi": "Bandung"
        }
    ]
    users = [
        {
            'user_id': '1ABCDEF', 
            'password': 'Mnsda1.da', 
            'email': 'user1@example.com', 
            'name': 'John', 
            'gender': 'Perempuan', 
            'usia': 28, 
            'phone_number': '081987654321',
            'gudang' : {
                "id" : "1",
                "nama" : "Gudang 1",
                "lokasi" : "Jakarta"
            }
        }
    ]

    pilihan_menu = 0
    global user_login
    #user_login = users[0]
    while True:
        if len(user_login) == 0:
            user_login = check_page(users, master_gudang)
        else:
            if pilihan_menu == 0:
                pilihan_menu = tampilkan_menu()
            elif pilihan_menu == 1:
                pilihan_menu = tampil_stok(stok)
            elif pilihan_menu == 2:
                pilihan_menu, stok = tambah_stok(stok, master_kategori)
            elif pilihan_menu == 3:
                pilihan_menu, stok = update_stok(stok, master_kategori)
            elif pilihan_menu == 4:
                pilihan_menu, stok = delete_stok(stok)
            elif pilihan_menu == 5:
                pilihan_menu, stok = transaction_stok(stok, "Transaksi Masuk")
            elif pilihan_menu == 6:
                pilihan_menu, stok = transaction_stok(stok, "Transaksi Keluar")
            else:
                return

def tampilkan_menu():
    data_table = {
            "title" : "Sistem Stock Gudang",
            "head" : ["no", "menu"],
            "rows" : [
                ["1", "Tampilkan Data Stock"],
                ["2", "Tambah Data Stock"],
                ["3", "Update Data Stock"],
                ["4", "Hapus Data Stock"],
                ["5", "Transaksi Masuk"],
                ["6", "Transaksi Keluar"],
                ["7", "Keluar"],
            ]
        }
    show_tabel(data_table)
    pilihan = input_validation({'label': 'Pilihan', "type" : "numeric", "equal_with" : [i[0] for i in data_table["rows"]]})
    return int(pilihan)

def show_tabel(datas):
    # set var title head row
    title = datas['title']
    header = datas['head']
    rows = datas['rows']

    # set max width agar responsive
    max_widths = [max(len(str(row_item)) for row_item in column) for column in zip(header, *rows)]
    total_width = sum(max_widths) + len(max_widths) * 3

    # menampilkan divider
    def divider_table():
        print(f"|{"-"*(total_width-1)}|")
    
    #menampilkan title
    print(f"|{title.title():^{total_width-1}}|")
    divider_table()

    # menampilkan header
    words = "|"
    for index, i in enumerate(header):
        words += f" { i.title() :^{max_widths[index]}} |"
    print(words)
    divider_table()

    # menampilkan baris 
    for i in rows:
        words = "|"
        for index, j in enumerate(i):
            words += f" {j:<{max_widths[index]}} |"
        print(words)
    divider_table()

def check_float(user_input):
    try:
        float(user_input)
        return True
    except:
        return False

def input_password():
    while True:
        password = input("Masukkan Password :")
        if len(password) <8:
            print("Password harus memiliki minimal 8 karakter.")
        elif not any(char.isdigit() for char in password):
            print("Password harus mengandung setidaknya satu angka.")
        elif not any(char.isupper() for char in password):
            print("Password harus mengandung setidaknya satu huruf kapital.")
        elif not any(char.islower() for char in password):
            print("Password harus mengandung setidaknya satu huruf kecil.")
        elif not any(char in "/.,@#$%" for char in password):
            print("Password harus mengandung setidaknya satu karakter khusus (/.,@#$%).")
        else:
            return password
        
def input_email():
    while True:
        email = input("Masukkan Email :")

        #cek format email
        if (
            len(email) < 1
            or email.count("@") < 1
            or email.count("@") > 1
            or email[email.index("@") + 1 : ].count(".") < 1
        ):
            print("Format email salah")
            continue

        #set variabel
        username = email[: email.index("@")]
        hosting = email[email.index("@") + 1 : email.index(".")]
        ekstensi = email[email.index("@") + 1 : ].replace(hosting, "")

        #cek format username
        if(
            len(username) < 1
            or not all(char.isalnum() or char in ['_', '.'] for char in username)
            or not username[0].isalnum()
        ):
            print("Format Username yg anda masukkan salah")
        #cek format hosting
        elif(
            len(hosting) < 1
            or not hosting.isalnum()
        ):
            print("Format Hosting yang anda masukan salah")
        #cek format ekstensi
        elif(
            len(ekstensi) < 1
            or not ekstensi.replace(".", "").isalnum()
            or any(len(char) > 5 or len(char) < 1 for char in ekstensi[1:].split("."))
            or ekstensi.count(".") > 2
        ):
            print("Format Ekstensi yang anda masukan salah")
        #validasi berhasil
        else:
            return email

def input_validation(validations):
    if validations['type'] == "email":
        return input_email()
    elif validations['type'] == "password":
        return input_password()
    else:
        valid = False
        while not valid:
            user_input = input(f"Masukkan {validations['label']} : ")
            # check type
            if "type" in validations.keys() and len(validations['type']) > 0:
                if validations["type"] == "alphabet" and user_input.replace(" ", "").isalpha():
                    valid = True
                elif validations["type"] == "alpha numeric" and user_input.replace(" ", "").isalnum():
                    valid = True
                elif validations["type"] == "numeric" and user_input.isnumeric():
                    valid = True
                elif validations["type"] == "float" and check_float(user_input):
                    valid = True
                else:
                    print(f"{validations['label']} hanya bisa berisi {validations['type']}")
                    valid = False
            else:
                valid = True
            # max value
            if "max" in validations.keys() and valid:
                if int(user_input) <= validations['max']:
                    valid = True
                else:
                    print(f"{validations['label']} maksimal {validations['max']}")
                    valid = False

            # min value
            if "min" in validations.keys() and valid:
                if int(user_input) >= validations['min']:
                    valid = True
                else:
                    print(f"{validations['label']} minimal {validations['min']}")
                    valid = False
            #same value
            if "equal_with" in validations.keys() and valid:
                if user_input in validations['equal_with']:
                    valid = True
                else:
                    print(f"{validations['label']} hanya bisa {', '.join(validations['equal_with'])}")
                    valid = False 
            #not same value
            if "not_equal_with" in validations.keys() and valid:
                if user_input not in validations['not_equal_with']:
                    valid = True
                else:
                    if validations['label'] == 'User Id':
                        print("User ID sudah digunakan. Silakan gunakan User ID lain")
                    else:
                        print(f"{validations['label']} {', '.join(validations['not_equal_with'])} sudah digunakan, silahkan coba lagi")
                    valid = False 

            # max length
            if "max_length" in validations.keys() and valid:
                if len(user_input) <= validations['max_length']:
                    valid = True
                else:
                    print(f"{validations['label']} maksimal {validations['max_length']} karakter")
                    valid = False

            # min length
            if "min_length" in validations.keys() and valid:
                if len(user_input) >= validations['min_length']:
                    valid = True
                else:
                    print(f"{validations['label']} minimal {validations['min_length']} karakter")
                    valid = False
            
            #equal length
            if "equal_length" in validations.keys() and valid:
                if len(user_input) == validations['equal_length']:
                    valid = True
                else:
                    print(f"{validations['label']} harus sama dengan {validations['equal_length']} karakter")
                    valid = False
            
            #must contain
            if "must_contain" in validations.keys() and valid:
                if any(char in validations['must_contain'] for char in user_input):
                    valid = True
                else:
                    print(f"{validations['label']} harus mengandung {validations['must_contain']}")
                    valid = False 
            #not must contain
            if "not_must_contain" in validations.keys() and valid:
                if not any(char in validations['not_must_contain'] for char in user_input):
                    valid = True
                else:
                    update_index = validations['not_must_contain'].index(" ")
                    validations['not_must_contain'][update_index] = "spasi"
                    print(f"{validations['label']} tidak boleh mengandung {', '.join(validations['not_must_contain'])}")
                    valid = False 

            # return jika valid
            if valid:
                return user_input

def check_page(users, master_gudang):
    
    while True:
        show_tabel(
            {
                "title" : "Selamat Datang",
                "head" : ["no", "menu"],
                "rows" : [
                    ["1", "Login"],
                    ["2", "Register"],
                ]
            }
        )
        print("Silahkan login untuk masuk sistem dan register untuk daftar terlebih dahulu")
        pilihan = input_validation({'label': 'pilihan', "type" : "numeric", "equal_with" : ["1", "2"]})
        pilihan = int(pilihan)
        if pilihan == 1:
            return login_page(users)
        elif pilihan == 2:
            register_page(users, master_gudang)

def login_page(users):
    print(f"{"-"*4}Login{"-"*4}")
    #check user id
    valid = 0
    while valid < 2:
        user_id = input_validation({'label':'User Id', 'type': 'alpha numeric', 'min_length' : 5, 'not_must_contain': [" "]})
        password = input_validation({'label':'Password', 'type': 'password'})
        list_user_id = [user['user_id'] for user in users]
        if user_id in list_user_id:
            index_user_id = list_user_id.index(user_id)
            #check password
            if users[index_user_id]['password'] == password:
                user = users[index_user_id]
                print("Login berhasil!")
                print("Detail Pengguna:")
                print(f"User ID: {user['user_id']}")
                print(f"Nama: {user['name']}")
                print(f"Email: {user['email']}")
                print(f"Jenis Kelamin: {user['gender']}")
                print(f"Usia: {user['usia']}")
                print(f"Phone Number: {user['phone_number']}")
                print("Gudang")
                print(f"Nama Gudang: {user['gudang']['nama']}")
                print(f"Lokasi Gudang: {user['gudang']['lokasi']}")
                return user
            else:
                print("Password Salah")


        else:
            print("ID tidak terdaftar")


def register_page(users, master_gudang):
    print(f"{"-"*4}Register{"-"*4}")
    user_id = input_validation({'label':'User Id', 'type': 'alpha numeric', 'not_equal_with' : [user['user_id'] for user in users], 'min_length' : 5, 'not_must_contain': [" "]})
    password = input_validation({'label':'Password', 'type': 'password'})
    email = input_validation({'label':'Email', 'type': 'email'})
    name = input_validation({'label':'Name', 'type': 'alphabet', 'min_length' : 5})
    gender = input_validation({'label': 'Gender (Pria/Wanita)', "type" : "alphabet", "equal_with" : ["Pria", "Wanita"]})
    usia = input_validation({'label':'Usia', 'type': 'numeric', 'min' : 17, 'max' : 80})
    phone_number = input_validation({'label':'No Handphone', 'type': 'numeric', 'min_length' : 11, 'max_length' : 13})
    print("Lokasi Gudang :")
    for i in master_gudang:
        print(f"{i['id']}. {i['nama']} {i['lokasi']}")
    gudang = input_validation({'label': 'Pilih Gudang', "type" : "numeric", "equal_with" : [i['id'] for i in master_gudang]})
    save_data = input_validation({'label':'Simpan Data (y/n)', 'type': 'alphabet', 'equal_with': ['y', 'n']})
    if save_data == "y":
        users.append({
            'user_id': user_id,
            'password': password,
            'email': email,
            'name': name,
            'gender': gender,
            'usia': usia,
            'phone_number': phone_number,
            'gudang': {
                "id" : gudang,
                "nama" : [i['nama'] for i in master_gudang if i['id'] == gudang][0],
                "lokasi" : [i['lokasi'] for i in master_gudang if i['id'] == gudang][0]
            }
        })
        print("Register berhasil, data tersimpan")

def tampil_stok(stok):
    def data_row_append(i):
        return [
            i['id'],
            i['nama_barang'],
            i['kategori']['nama'],
            i['vendor'],
            i['gudang']['nama'],
            i['stok'],
            f"{i['update_by']['id']} ({i['update_by']['name']})"
        ]

    while True:
        data_table = {
                "title" : "Report Data Stok",
                "head" : ["No", "Menu"],
                "rows" : [
                    ["1", "Report seluruh data"],
                    ["2", "Report data tertentu"],
                    ["3", "Report detail transaksi"],
                    ["99", "Kembali ke menu utama"],
                ]
            }
        show_tabel(data_table)
        pilihan = int(input_validation({'label': 'Pilihan', "type" : "numeric", "equal_with" : [i[0] for i in data_table["rows"]]}))
        if pilihan == 1:
            data_row = []
            for i in stok:
                data_row.append(data_row_append(i))
            data_table = {
                "title" : "Data All Stok",
                "head" : ["id", "Nama Barang", "Kategori", "Vendor", "Gudang", "Stok", "Last Update By"],
                "rows" : data_row
            }
            show_tabel(data_table)
            pilihan = int(input_validation({'label': 'Back (99)', "type" : "numeric", "equal_with" : ["99"]}))
        
        elif pilihan == 2:
            data_table = {
                "title" : "Filter by",
                "head" : ["No", "Menu"],
                "rows" : [
                    ["1", "Id"],
                    ["2", "Nama"],
                    ["3", "Kategori"],
                    ["4", "Vendor"],
                    ["5", "Gudang"],
                    ["99", "Back"],
                ]
            }
            show_tabel(data_table)
            pilihan = int(input_validation({'label': 'Pilihan', "type" : "numeric", "equal_with" : [i[0] for i in data_table["rows"]]}))
            if pilihan != 99:
                find_by = input_validation({'label': data_table['rows'][int(pilihan)-1][1], "type" : "", 'min_length': 1})
                data_row = []
                for i in stok:
                    if pilihan == 1 and i['id'] == find_by:
                        data_row.append(data_row_append(i))
                    elif pilihan == 2 and i['nama_barang'] == find_by:
                        data_row.append(data_row_append(i))
                    elif pilihan == 3 and i['kategori']['nama'] == find_by:
                        data_row.append(data_row_append(i))
                    elif pilihan == 4 and i['vendor'] == find_by:
                        data_row.append(data_row_append(i))
                    elif pilihan == 5 and i['gedung']['nama'] == find_by:
                        data_row.append(data_row_append(i))
                
                
                data_table = {
                    "title" : f"Data Stok by {data_table['rows'][int(pilihan)-1][1]}",
                    "head" : ["id", "Nama Barang", "Kategori", "Vendor", "Gudang", "Stok", "Last Update By"],
                    "rows" : data_row
                }
                show_tabel(data_table)
                pilihan = int(input_validation({'label': 'Back (99)', "type" : "numeric", "equal_with" : ["99"]}))
            
        elif pilihan == 3:
            id = input_validation({'label':'Id Barang', 'type': 'alpha numeric', 'min_length' : 5})
            stok_detail = [i for i in stok if i['id'] == id]
            if len(stok_detail) > 0:
                data_row = []
                for i in stok_detail[0]['transaction']:
                    data_row.append(
                        [
                            i['tipe'],
                            i['jumlah'],
                            i['input_by']['name']
                        ]
                    )
                data_table = {
                    "title" : f"Data Stok ID {id}",
                    "head" : ["Tipe Transaksi", "Total", "Input By"],
                    "rows" : data_row
                }
                show_tabel(data_table)
                pilihan = int(input_validation({'label': 'Back (99)', "type" : "numeric", "equal_with" : ["99"]}))
            else:
                print("Id Barang tidak ditemukan")

        elif pilihan == 99:
            return 0


def tambah_stok(stok, master_kategori):
    print(f"{"-"*4}Tambah Stok{"-"*4}")
    id = input_validation({'label':'Id Barang', 'type': 'alpha numeric', 'not_equal_with' : [i['id'] for i in stok], 'min_length' : 5, 'not_must_contain': [" "]})
    nama_barang = input_validation({'label':'Nama Barang', 'type': 'alphabet', 'min_length' : 5})
    print("Kategori Barang:")
    for kategori in master_kategori:
        print(f"{kategori['id']} - {kategori['nama']}")
    kategori = input_validation({'label': 'Kategori Barang', "type" : "numeric", "equal_with" : [i['id'] for i in master_kategori]})
    vendor = input_validation({'label':'Vendor Barang', 'type': 'alphabet', 'min_length' : 5})
    stok.append({
        'id': id,
        'nama_barang': nama_barang,
        'kategori': {
            "id" : kategori,
            "nama" : [i['nama'] for i in master_kategori if i['id'] == kategori][0]
        },
        'vendor': vendor,
        'gudang' : user_login['gudang'],
        'stok' : 0,
        'transaction' : [],
        'input_by' : {
            'id' : user_login['user_id'],
            'name' : user_login['name']
        },
        'update_by' : {
            'id' : user_login['user_id'],
            'name' : user_login['name']
        },
    })

    print("Data stock berhasil ditambahkan.")
    return 0, stok

def update_stok(stok, master_kategori):
    print(f"{"-"*4}Update Stok{"-"*4}")
    id = input_validation({'label':'Id Barang', 'type': 'alpha numeric', 'min_length' : 5})
    stok_detail = [i for i in stok if i['id'] == id]
    if len(stok_detail) > 0:
        if stok_detail[0]['gudang'] == user_login['gudang']:
            nama_barang = input_validation({'label':'Nama Barang', 'type': 'alphabet', 'min_length' : 5})
            print("Kategori Barang:")
            for kategori in master_kategori:
                print(f"{kategori['id']} - {kategori['nama']}")
            kategori = input_validation({'label': 'Kategori Barang', "type" : "numeric", "equal_with" : [i['id'] for i in master_kategori]})
            vendor = input_validation({'label':'Vendor Barang', 'type': 'alphabet', 'min_length' : 5})
            stok_index = [i['id'] for i in stok]
            stok_index = stok_index.index(id)
            stok[stok_index]['nama_barang'] = nama_barang
            stok[stok_index]['kategori']['id'] = kategori
            stok[stok_index]['kategori']['nama'] = [i['nama'] for i in master_kategori if i['id'] == kategori][0]
            stok[stok_index]['vendor'] = vendor
            stok[stok_index]['update_by'] = {
                'id' : user_login['user_id'],
                'name' : user_login['name']
            }
            print("Update success")
        else:
            print("Tidak mempunyai hak akses update, karena berbeda gudang")
    else:
        print("Id barang tidak ditemukan.")
    return 0, stok

def delete_stok(stok):
    print(f"{"-"*4}Delete Stok{"-"*4}")
    id = input_validation({'label':'Id Barang', 'type': 'alpha numeric', 'min_length' : 5})
    stok_detail = [i for i in stok if i['id'] == id]
    if len(stok_detail) > 0:
        if stok_detail[0]['gudang'] == user_login['gudang']:
            stok_index = [i['id'] for i in stok]
            stok_index = stok_index.index(id)
            del stok[stok_index]
        else:
            print("Tidak mempunyai hak akses update, karena berbeda gudang")
    else:
        print("Id barang tidak ditemukan.")
    return 0, stok

def transaction_stok(stok, type):
    print(f"{"-"*4} {type} Stok{"-"*4}")
    id = input_validation({'label':'Id Barang', 'type': 'alpha numeric', 'min_length' : 5})
    stok_detail = [i for i in stok if i['id'] == id]
    if len(stok_detail) > 0:
        if stok_detail[0]['gudang'] == user_login['gudang']:
            total = int(input_validation({'label': f"Jumlah {type}", 'type': 'numeric', 'min' : 1}))
            stok_index = [i['id'] for i in stok]
            stok_index = stok_index.index(id)
            if type == "Transaksi Masuk":
                stok[stok_index]['stok'] += total
            else:
                stok[stok_index]['stok'] -= total
            stok[stok_index]['transaction'].append({
                'tipe': type,
                'jumlah': total,
                'input_by': {
                    'id' : user_login['user_id'],
                    'name' : user_login['name']
                }
            })
            print("Update success")
        else:
            print("Tidak mempunyai hak akses update, karena berbeda gudang")
    else:
        print("Id barang tidak ditemukan.")
    return 0, stok

#start

main()
