import random

def get_computer_choice():
    """Get a random choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_emoji(choice):
    """Return emoji for the choice."""
    emojis = {
        "rock": "🪨",
        "paper": "📄",
        "scissors": "✂️"
    }
    return emojis.get(choice, "")

def determine_winner(user_choice, computer_choice):
    """Determine the winner of a round."""
    if user_choice == computer_choice:
        return "tie"
    
    # Define winning conditions
    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if winning_moves[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"

def play_round(user_choice, user_score, computer_score):
    """Play a single round."""
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    # Display choices with emojis
    print(f"\nYou chose:     {get_emoji(user_choice)} {user_choice.upper()}")
    print(f"Computer chose: {get_emoji(computer_choice)} {computer_choice.upper()}")
    print("-" * 35)
    
    # Determine outcome
    if result == "user":
        print("🎉 YOU WIN THIS ROUND! 🎉")
        user_score += 1
    elif result == "computer":
        print("💻 COMPUTER WINS THIS ROUND!")
        computer_score += 1
    else:
        print("🤝 IT'S A TIE!")
    
    print(f"Score: You {user_score} - Computer {computer_score}")
    
    return user_score, computer_score

def display_final_results(user_score, computer_score):
    """Display final game results."""
    print("\n" + "="*40)
    print("🏆 FINAL RESULTS 🏆")
    print("="*40)
    print(f"Your Score:      {user_score}")
    print(f"Computer Score:  {computer_score}")
    
    if user_score > computer_score:
        print("\n🥇 YOU WIN THE MATCH! AWESOME! 🥇")
    elif computer_score > user_score:
        print("\n🤖 COMPUTER WINS THIS TIME! BETTER LUCK NEXT TIME! 🤖")
    else:
        print("\n🤝 IT'S A TIE! WELL PLAYED! 🤝")
    print("="*40 + "\n")

def main():
    """Main game loop."""
    print("\n" + "="*40)
    print("🎮 ROCK PAPER SCISSORS 🎮")
    print("="*40)
    print("\nBattle against the computer!\n")
    
    user_score = 0
    computer_score = 0
    
    valid_choices = ["rock", "paper", "scissors"]
    
    while True:
        user_input = input("Your turn! Type Rock/Paper/Scissors or Q to quit: ").strip().lower()
        
        # Check for quit
        if user_input == "q":
            display_final_results(user_score, computer_score)
            print("👋 Thanks for playing! See you next time!\n")
            break
        
        # Validate input
        if user_input not in valid_choices:
            print("❌ Invalid choice! Please enter rock, paper, or scissors.\n")
            continue
        
        # Play the round
        user_score, computer_score = play_round(user_input, user_score, computer_score)

if __name__ == "__main__":
    main()
