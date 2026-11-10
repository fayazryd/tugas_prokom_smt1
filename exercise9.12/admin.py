from user import User


class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Hak akses admin:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Administrator, jenis khusus dari pengguna."""

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()