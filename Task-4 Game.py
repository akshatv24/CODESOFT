# Task 4: Rock-Paper-Scissors
import random

print("--- Rock, Paper, Scissors Game ---")
user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

while True:
    print("\nScore -> You:", user_score, "| Computer:", computer_score)
    user_choice = input("Enter rock, paper, or scissors (or type 'quit' to stop): ").lower()
    
    if user_choice == 'quit':
        print("Thanks for playing!")
        break
        
    if user_choice not in options:
        print("Invalid input. Please try again.")
        continue
        
    comp_choice = random.choice(options)
    print("Computer chose:", comp_choice)
    
    # Game Logic
    if user_choice == comp_choice:
        print("It's a tie!")
    elif user_choice == "rock" and comp_choice == "scissors":
        print("Rock beats scissors! You win.")
        user_score += 1
    elif user_choice == "scissors" and comp_choice == "paper":
        print("Scissors beat paper! You win.")
        user_score += 1
    elif user_choice == "paper" and comp_choice == "rock":
        print("Paper beats rock! You win.")
        user_score += 1
    else:
        print("You lose this round.")
        computer_score += 1