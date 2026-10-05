print("TELEMETRY FAILURE!!!"),
print("UNABLE TO DECYPHER ENCRYPTION. DEFAULTING TO LOGIC MODE")
print("Logic mode activated. Please follow the instructions carefully.")
Name = input("What is your name?:      ")
print("Welcome, " + Name + "!")
print ("I am Apollo, your assistant. Activated once Telemetry failure was detected. Let us get basic archival systems back online. ")
print(" Think of a number that once you multiply it by 6 and subtract it by 12, the result will be exactly the same as adding 20 to its double. What is the answer?")
attempts = 0
max_attempts = 3
success = False
while attempts < max_attempts and not success:
    passcode =input("Enter your answer:  ")

    if not passcode.isdigit():
        attempts += 1
        print ("HINT: The answer is a positive integer.")
        continue
    if int(passcode) ==8:
        print("Archive systems restored. You may now proceed to the next level.")
        success = True
    else:
        attempts +=1
        print("Wrong answer, the answer is a positive integer")
    

if not success:
    print("TOTAL ENCRYPTION FAILURE, ALL DATA LOST ")
    