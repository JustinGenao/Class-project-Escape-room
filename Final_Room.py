print("\n--- ROOM 3:THE ESCAPE DOOR ---")
print("You enter a large metal room.")
print("There is a massive metal door in front of you.")
print("Next to it is a mysterious WHITE BUTTON.")
print("A screen flashes: 10 SECONDS REMAINING.")
print("What do you do?")
print("1. Press the white button")
print("2. Do nothing")

choice = input("Choose 1 or 2: ")

if choice == "1":
    print("\nBEEP! BEEP! BEEP!")
    print("The button activates the security alarm!")
    print("GAME OVER!")

elif choice == "2":
    print("\nYou chose to leave the button alone.")
    print("10 seconds pass...")
    print("CLICK!")
    print("The massive metal door opens.")
    print("You escaped SUCCESSFULLY!")

else:
    print("\nYou hesitate for too long...")
    print("GAME OVER!")
