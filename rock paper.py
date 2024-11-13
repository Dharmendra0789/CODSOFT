import random
#determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main program
choices = ["rock", "paper", "scissors"]

while True:
    # Get player input
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

    if player_choice == "quit":
        print("Thanks for playing!")
        break

    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    # Get computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine winner and display result
    result = determine_winner(player_choice, computer_choice)
    print(result)
