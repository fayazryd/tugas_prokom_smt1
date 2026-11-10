class Admin(User):

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Hak akses admin {self.first_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin('Rina', 'Kusuma', 28, 'Jakarta')
admin.show_privileges()