print(" SECOND DOOR: WIRE CHALLENGE")

print("Choose the correct wire before time runs out!")

print("RED or BLUE")

correct_wire = random.choice(["red", "blue"])

start = time.time()

choice = input("Which wire will you cut? ").lower()

end = time.time()

if end - start > 5:

    print(" Too slow! Hacker detected. GAME OVER!")

elif choice == correct_wire:

    print(" Correct wire! Door unlocked.")

else:

    print(" Wrong wire!")

    print("The correct wire was:", correct_wire)

    print("Hacker detected. GAME OVER!")
