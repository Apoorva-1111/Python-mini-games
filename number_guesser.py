import random

def get_difficulty():
    """Let player choose difficulty level."""
    print("\n🎮 Choose Difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")
    
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == '1':
            return 50
        elif choice == '2':
            return 100
        elif choice == '3':
            return 500
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

def get_range():
    """Get custom range from player."""
    while True:
        user_input = input("Enter the max number: ").strip()
        if user_input.isdigit():
            max_num = int(user_input)
            if max_num > 0:
                return max_num
            else:
                print("❌ Please enter a number larger than 0.")
        else:
            print("❌ Please enter a valid number.")

def get_hint(secret, guess):
    """Provide helpful feedback about the guess."""
    diff = abs(secret - guess)
    if diff == 0:
        return "🎯 Perfect!"
    elif diff <= 5:
        return "🔥 Burning hot! Very close!"
    elif diff <= 15:
        return "☀️  Warm, getting closer!"
    elif diff <= 30:
        return "🌤️  Lukewarm, keep trying!"
    else:
        return "❄️  Cold! Try a different range."

def play_game():
    """Main game loop."""
    print("\n" + "="*40)
    print("🎲 WELCOME TO NUMBER GUESSER! 🎲")
    print("="*40)
    
    # Get difficulty
    print("\nWould you like to:")
    print("1. Choose difficulty")
    print("2. Enter custom max number")
    mode = input("Choose 1 or 2: ").strip()
    
    if mode == '1':
        max_num = get_difficulty()
    else:
        max_num = get_range()
    
    # Generate random number
    secret_number = random.randint(1, max_num)
    guesses = 0
    max_guesses = len(str(max_num)) * 5  # Suggested max based on range
    
    print(f"\n✨ I'm thinking of a number between 1 and {max_num}...")
    print(f"💡 Tip: You should find it in about {max_guesses} guesses or less!\n")
    
    # Game loop
    while True:
        guesses += 1
        
        try:
            guess = input(f"Guess #{guesses}: ").strip()
            
            if not guess.isdigit():
                print("❌ Please enter a valid number!")
                guesses -= 1  # Don't count invalid input
                continue
            
            guess = int(guess)
            
            if guess < 1 or guess > max_num:
                print(f"❌ Number must be between 1 and {max_num}!")
                guesses -= 1
                continue
            
            # Check the guess
            if guess == secret_number:
                print(f"\n🎉🎉🎉 YOU GOT IT! 🎉🎉🎉")
                print(f"The number was {secret_number}!")
                print(f"⭐ You found it in {guesses} guesses!")
                
                if guesses == 1:
                    print("🤯 WOW! Lucky first guess!")
                elif guesses <= max_guesses // 2:
                    print("🏆 Excellent guessing!")
                elif guesses <= max_guesses:
                    print("👍 Good job!")
                else:
                    print("💪 You did it!")
                break
            elif guess > secret_number:
                direction = "⬇️  TOO HIGH!"
                hint = get_hint(secret_number, guess)
                print(f"{direction} {hint}")
            else:
                direction = "⬆️  TOO LOW!"
                hint = get_hint(secret_number, guess)
                print(f"{direction} {hint}")
        
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for playing!")
            return False

def main():
    """Main program."""
    while True:
        play_game()
        
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\n🎮 Thanks for playing! See you next time! 👋\n")
            break

if __name__ == "__main__":
    main()
