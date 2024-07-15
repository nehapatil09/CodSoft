import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    global user_score, computer_score
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to make your choice.")
    print("Type 'exit' to quit the game at any time.\n")
    
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice == "exit":
            break
        while user_choice not in choices:
            user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()

        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a Tie!")
        elif winner == "user":
            print("You Win!")
            user_score += 1
        else:
            print("You Lose!")
            computer_score += 1

        print(f"Scores -> You: {user_score}, Computer: {computer_score}\n")

        play_again = input("Do you want to play another round? (Yes/No): ").lower()
        if play_again != "Yes":
            break

    print("\nThanks for Playing!")
    print(f"Final Scores -> You: {user_score}, Computer: {computer_score}")

play_game()
