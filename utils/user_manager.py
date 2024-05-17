import os
from utils.user import User

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists('data/users.txt'):
            open('data/users.txt', 'w').close()
        
        with open('data/users.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                self.users[username] = User(username, password)

    def save_users(self):
        with open('data/users.txt', 'w') as file:
            for username, user in self.users.items():
                file.write(f'{username},{user.password}\n')

    def validate_username(self, username):
        return len(username) >= 4

    def validate_password(self, password):
        return len(password) >= 8

    def register(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password)
        self.save_users()
        return True

    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            return True
        return False
