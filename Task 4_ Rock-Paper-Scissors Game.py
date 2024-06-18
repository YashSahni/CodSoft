import random
import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    print("Rock-Paper-Scissors Game")
    
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.choice_label = tk.Label(root, text="Choose rock, paper, or scissors:")
        self.choice_label.pack()

        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play('rock'))
        self.rock_button.pack()

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play('paper'))
        self.paper_button.pack()

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play('scissors'))
        self.scissors_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.score_label = tk.Label(root, text="Score: You 0 - 0 Computer")
        self.score_label.pack()

    def play(self, user_choice):
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        self.result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}. {result}")

        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1
        
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
