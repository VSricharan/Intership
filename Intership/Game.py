import random
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to get a valid user choice
def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose again.")

# Main game function with score tracking
def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nRock, Paper, Scissors Game")
        
        # Get user and computer choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Display choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine and display the result
        result = determine_winner(user_choice, computer_choice)
        print(f"\n{result}")
        
        # Update and display scores
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print(f"\nScores: You: {user_score} | Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    play_game()