import json


def get_new_username():
    username = input("Masukkan nama pengguna baru: ")

    with open("username.json", "w") as file:
        json.dump(username, file)

    return username


def greet_user():
    try:
        with open("username.json") as file:
            username = json.load(file)

        print("Apakah nama Anda", username, "?")
        jawaban = input("Masukkan ya atau tidak: ")

        if jawaban.lower() == "ya":
            print("Selamat datang kembali,", username)

        else:
            username = get_new_username()
            print("Nama berhasil diperbarui,", username)

    except FileNotFoundError:
        username = get_new_username()
        print("Selamat datang,", username)


greet_user()