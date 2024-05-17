import os
import datetime
import random
from utils.user_manager import UserManager
from utils.score import Score

class DiceGame:
    def __init__(self):
        self.user_manager = UserManager()
        self.scores = []
        self.current_user = None
        self.load_scores()

    def load_scores(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists('data/rankings.txt'):
            open('data/rankings.txt', 'w').close()
        
        with open('data/rankings.txt', 'r') as file:
            for line in file:
                username, game_id, points, wins = line.strip().split(',')
                self.scores.append(Score(username, game_id, int(points), int(wins)))
        self.scores.sort(key=lambda x: x.points, reverse=True)

    def save_scores(self):
        with open('data/rankings.txt', 'w') as file:
            for score in self.scores:
                file.write(f'{score.username},{score.game_id},{score.points},{score.wins}\n')

    def menu(self):
        while True:
            print("\n" + "="*30)
            print(f"Welcome, {self.current_user.username}!")
            print("="*30)
            print("1. Start Game\n2. Show Top Scores\n3. Log Out")
            print("="*30)
            choice = input("Enter your choice: ").strip()

            match choice:
                case '1':
                   self.play_game()
                case '2':
                   self.show_top_scores()
                case '3':
                   self.logout()
                   return
                case '_':
                    print("Invalid choice. Please try again.")

    def play_game(self):
        total_points = 0
        stages_won = 0
        game_id = f'{self.current_user.username}{datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")}'

        while True:
            user_wins = 0
            cpu_wins = 0

            while user_wins < 2 and cpu_wins < 2:
                user_roll = random.randint(1, 6)
                cpu_roll = random.randint(1, 6)
                print(f"\nUser rolled: {user_roll}")
                print(f"CPU rolled: {cpu_roll}")

                if user_roll > cpu_roll:
                    user_wins += 1
                    total_points += 1
                    print("You win this round!")
                elif cpu_roll > user_roll:
                    cpu_wins += 1
                    print("CPU wins this round!")
                else:
                    print("It's a tie!")

            if user_wins == 2:
                stages_won += 1
                total_points += 3
                print(f"\nYou won this stage! Total points: {total_points}, Stages won: {stages_won}")
                while True:
                    choice = input("Do you want to continue to the next stage? (1 for yes, 0 for no): ").strip()
                    if choice == '0':
                        break
                    elif choice == '1':
                        break
                    else:
                        print("Invalid choice. Please enter 1 for yes or 0 for no.")
            else:
                print("Game over. You didn't win any stages.")
                break

        if stages_won > 0:
            score = Score(self.current_user.username, game_id, total_points, stages_won)
            self.scores.append(score)
            self.scores.sort(key=lambda x: x.points, reverse=True)
            self.scores = self.scores[:10]  # Keep only top 10 scores
            self.save_scores()

    def show_top_scores(self):
        print("\n" + "="*30)
        print("Top Scores")
        print("="*30)
        if not self.scores:
            print("No games played yet. Play a game to see top scores.")
        else:
            for score in self.scores:
                print(f'User: {score.username}, Points: {score.points}, Wins: {score.wins}')
        input("Press Enter to continue...")

    def logout(self):
        self.current_user = None
        print("Logged out successfully.")
