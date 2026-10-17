import time
import random

name = input("Enter your name: ")


# ROOM 1: RIDDLE CHALLENGE
def room1():
    print(f"\nWelcome, {name}!")
    print("ROOM 1: THE RIDDLE CHALLENGE")

    time.sleep(1)
    print(f"Open the door and enter the room, {name}.")
    time.sleep(1)

    print("You must solve a riddle to pass Level 1!")
    time.sleep(2)

    print("\nRiddle:")
    print("You see 3 apples on a table and you take 2 for yourself, how many do you have?")
    print("You have 5 seconds to answer!")

    start = time.time()
    answer = input("> ").strip()
    end = time.time()

    if end - start > 5:
        print("Too slow! GAME OVER!")
        return False

    elif answer == "2":
        print("Correct! You passed Level 1!")
        return True

    else:
        print("Wrong answer! GAME OVER!")
        return False


# ROOM 2: WIRE CHALLENGE
def room2():
    print("\n--- ROOM 2: WIRE CHALLENGE ---")
    print("Choose the correct wire before time runs out!")
    print("RED or BLUE")

    correct_wire = random.choice(["red", "blue"])

    start = time.time()
    choice = input("Which wire will you cut? ").strip().lower()
    end = time.time()

    if end - start > 5:
        print("Too slow! Hacker detected. GAME OVER!")
        return False

    elif choice == correct_wire:
        print("Correct wire! Door unlocked!")
        return True

    else:
        print("Wrong wire!")
        print("The correct wire was:", correct_wire)
        print("Hacker detected. GAME OVER!")
        return False


# ROOM 3: THE ESCAPE DOOR
def room3():
    print("\n--- ROOM 3: THE ESCAPE DOOR ---")
    print("You enter a large metal room.")
    print("There is a massive metal door in front of you.")
    print("Next to it is a mysterious WHITE BUTTON.")

    print("\nA screen flashes: 10 SECONDS REMAINING.")
    print("What do you do?")
    print("1. Press the white button")
    print("2. Do nothing")

    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        print("\nBEEP! BEEP! BEEP!")
        print("The button activates the security alarm!")
        print("GAME OVER!")
        return False

    elif choice == "2":
        print("\nYou chose to leave the button alone.")
        print("10 seconds pass...")
        print("CLICK!")
        print("The massive metal door opens.")
        print(f"Congratulations, {name}! You escaped SUCCESSFULLY!")
        return True

    else:
        print("\nYou hesitate for too long...")
        print("GAME OVER!")
        return False


# MAIN GAME: CONNECT ALL THREE ROOMS
print("\nWelcome to the Escape Challenge!")

if room1():
    if room2():
        room3()

print("\nThanks for playing!")
