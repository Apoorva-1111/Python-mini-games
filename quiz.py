print("Welcome to the quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does BIOS stand for? ")
if answer.lower() == "basic input output system":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does USB stand for? ")
if answer.lower() == "universal serial bus":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does LAN stand for? ")
if answer.lower() == "local area network":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does WAN stand for? ")
if answer.lower() == "wide area network":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does HTTP stand for? ")
if answer.lower() == "hypertext transfer protocol":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does HTTPS stand for? ")
if answer.lower() == "hypertext transfer protocol secure":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does CSS stand for? ")
if answer.lower() == "cascading style sheets":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does SQL stand for? ")
if answer.lower() == "structured query language":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does API stand for? ")
if answer.lower() == "application programming interface":
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