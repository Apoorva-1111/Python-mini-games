def run_quiz():
    """Run a technology acronym quiz game."""
    print("\n" + "="*50)
    print("🧠 TECH ACRONYM QUIZ 🧠")
    print("="*50)
    print("\nTest your knowledge of technology terms!\n")
    
    playing = input("Do you want to play? (yes/no): ").strip().lower()
    
    if playing not in ['yes', 'y']:
        print("👋 Maybe next time!\n")
        return
    
    # Quiz questions and answers
    questions = [
        ("What does CPU stand for?", "central processing unit"),
        ("What does GPU stand for?", "graphics processing unit"),
        ("What does RAM stand for?", "random access memory"),
        ("What does PSU stand for?", "power supply"),
        ("What does HDD stand for?", "hard disk drive"),
        ("What does SSD stand for?", "solid state drive"),
        ("What does ROM stand for?", "read only memory"),
        ("What does BIOS stand for?", "basic input output system"),
        ("What does USB stand for?", "universal serial bus"),
        ("What does LAN stand for?", "local area network"),
        ("What does WAN stand for?", "wide area network"),
        ("What does HTTP stand for?", "hypertext transfer protocol"),
        ("What does HTTPS stand for?", "hypertext transfer protocol secure"),
    ]
    
    score = 0
    total = len(questions)
    
    print(f"Okay! Let's play! 🎮 ({total} questions)\n")
    
    # Ask each question
    for i, (question, correct_answer) in enumerate(questions, 1):
        user_answer = input(f"Q{i}: {question} ").strip().lower()
        
        if user_answer == correct_answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect! The answer is: {correct_answer.upper()}\n")
    
    # Display results
    print("="*50)
    print("📊 QUIZ RESULTS 📊")
    print("="*50)
    percentage = (score / total) * 100
    print(f"Your Score: {score}/{total} ({percentage:.1f}%)\n")
    
    if percentage == 100:
        print("🏆 PERFECT! You're a tech expert! 🏆")
    elif percentage >= 80:
        print("🌟 Excellent! You really know your tech!")
    elif percentage >= 60:
        print("👍 Good job! You know quite a bit!")
    elif percentage >= 40:
        print("💪 Not bad! Keep learning!")
    else:
        print("📚 Keep studying! You'll get better!")
    print()

def main():
    """Main program."""
    while True:
        run_quiz()
        
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("👋 Thanks for playing! See you next time!\n")
            break

if __name__ == "__main__":
    main()
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GUI stand for? ")
if answer.lower() == "graphical user interface":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does CLI stand for? ")
if answer.lower() == "command line interface":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does IDE stand for? ")
if answer.lower() == "integrated development environment":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 20) * 100) + "%.")
