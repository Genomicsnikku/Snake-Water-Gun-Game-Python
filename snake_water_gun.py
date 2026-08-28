# ==========================================================
# PROJECT 1: SNAKE, WATER, GUN GAME
# A Python implementation of the classic childhood game.
# ==========================================================

import random

def get_computer_choice():
    """Generates a random choice for the computer: 
    's' for Snake, 'w' for Water, 'g' for Gun.
    """
    choices = ['s', 'w', 'g']
    return random.choice(choices)

def get_user_choice():
    """Takes and validates the user's choice from the input."""
    while True:
        user_input = input("Enter your choice ('s' for Snake, 'w' for Water, 'g' for Gun): ").lower()
        if user_input in ['s', 'w', 'g']:
            return user_input
        print("Invalid choice! Please try again with 's', 'w', or 'g'.")

def determine_winner(user, computer):
    """Determines the winner based on Snake, Water, Gun rules:
    - Snake drinks Water -> Snake wins (s > w)
    - Water douses Gun -> Water wins (w > g)
    - Gun kills Snake -> Gun wins (g > s)
    """
    if user == computer:
        return "It's a Draw!"
    
    # Winning conditions for the user
    if (user == 's' and computer == 'w') or \
       (user == 'w' and computer == 'g') or \
       (user == 'g' and computer == 's'):
        return "Congratulations! You Win! 🎉"
    
    return "Computer Wins! Better luck next time. 🤖"

def play_game():
    """Main function to run the Snake, Water, Gun game loop."""
    print("==========================================")
    print("   WELCOME TO SNAKE, WATER, GUN GAME      ")
    print("==========================================")
    print("Rules:")
    print(" 1. Snake (s) drinks Water (w) -> Snake wins")
    print(" 2. Water (w) damages Gun (g)  -> Water wins")
    print(" 3. Gun (g) shoots Snake (s)   -> Gun wins")
    print("-" * 42)

    # Dictionary for mapping short codes to full names for display
    name_mapping = {'s': 'Snake 🐍', 'w': 'Water 💧', 'g': 'Gun 🔫'}

    # Get choices
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    # Display choices
    print(f"\nYou chose: {name_mapping[user_choice]}")
    print(f"Computer chose: {name_mapping[computer_choice]}")
    print("-" * 42)

    # Determine and print result
    result = determine_winner(user_choice, computer_choice)
    print(result)
    print("==========================================")

# Execute the game
if __name__ == "__main__":
    play_game()
      
