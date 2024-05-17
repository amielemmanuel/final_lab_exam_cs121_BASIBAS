from utils.dice_game import DiceGame

def main():
    game = DiceGame()
    main_menu(game)

def main_menu(game):
    while True:
        print("="*30 + "\n" + " WELCOME TO DICE ROLL GAME! " + "\n" +"="*30)
        print("1. Register\n2. Login\n3. Exit")
        print("=" * 30)
        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                register(game)
            case '2':
                login(game)
            case '3':
                print("SYSTEM CLOSE")
                break
            case '_':
                print("INVALID CHOICE. Please try again.")    

def register(game):
    while True:
        print("="*30 + "\n" + " REGISTER " + "\n" +"="*30)
        username = input("Enter username (at least 4 characters long), or leave blank to cancel: ").strip()
        if username == "":
            return
        if not game.user_manager.validate_username(username):
            print("Username must be at least 4 characters long.")
            continue

        password = input("Enter password (at least 8 characters long), or leave blank to cancel: ").strip()
        if password == "":
            return
        if not game.user_manager.validate_password(password):
            print("Password must be at least 8 characters long.")
            continue

        if game.user_manager.register(username, password):
            print("REGISTERED SUCCESSFULLY!")
            return
        else:
            print("USERNAME ALREADY EXISTS Please try again.")

def login(game):
    while True:
        print("="*30 + "\n" + " LOGIN " + "\n" +"="*30)
        username = input("Enter username (leave blank to cancel): ").strip()
        if username == "":
            return

        password = input("Enter password (leave blank to cancel): ").strip()
        if password == "":
            return

        if game.user_manager.login(username, password):
            game.current_user = game.user_manager.users[username]
            game.menu()
            return
        else:
            print("INVALID USERNAME OR PASSWORD. Please try again.")

if __name__ == "__main__":
    main()
