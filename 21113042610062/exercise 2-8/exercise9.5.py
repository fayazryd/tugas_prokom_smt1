class User:
    """Profil pengguna sederhana."""

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def increment_login_attempts(self):
        """Tambah percobaan login sebanyak 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Kembalikan percobaan login ke 0."""
        self.login_attempts = 0


user = User('Budi', 'Santoso', 25, 'Semarang')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Percobaan login: {user.login_attempts}")

user.reset_login_attempts()
print(f"Percobaan login setelah reset: {user.login_attempts}")