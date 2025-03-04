import random
choices = ["rock", "paper", "scissors"]
user = input("Enter rock, paper, or scissors: ").lower()
ai_choice = random.choice(choices)
print(f"AI chose {ai_choice}")

if user == ai_choice:
    print("It's a tie!")
elif (user == "rock" and ai_choice == "scissors") or (user == "scissors" and ai_choice == "paper") or (user == "paper" and ai_choice == "rock"):
    print("You win!")
else:
    print("AI wins!")
