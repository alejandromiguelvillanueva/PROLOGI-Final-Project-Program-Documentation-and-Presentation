class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def login(users):
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in users:
            if user.username == username and user.password == password:
                print(f"Welcome, {username}!")
                return True
        print("Invalid username or password. Please try again.")
