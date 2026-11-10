class User:
    def __init__(self, first_name, last_name, age, city, pekerjaan):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.pekerjaan = pekerjaan

    def describe_user(self):
        print("Nama depan:", self.first_name)
        print("Nama belakang:", self.last_name)
        print("Umur:", self.age)
        print("Kota:", self.city)
        print("Pekerjaan:", self.pekerjaan)

    def greet_user(self):
        print("Halo", self.first_name, self.last_name,
              "! Selamat datang kembali.")


user1 = User("Fayaz", "Rasyid", 19, "Semarang", "Mahasiswa")
user2 = User("Andi", "Pratama", 20, "Solo", "Mahasiswa")
user3 = User("Budi", "Santoso", 25, "Jakarta", "Karyawan")


user1.describe_user()
user1.greet_user()

print()

user2.describe_user()
user2.greet_user()

print()

user3.describe_user()
user3.greet_user()