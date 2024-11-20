import random  # Import the random module to generate random numbers

# Greet the user
print("Hi, welcome to the number guessing game!")

# Generate a random number between 0 and 99
guess = random.randint(0, 100)  
counter = 0  # Initialize counter to keep track of the number of guesses
chances = 10

# Start the game loop
while counter < chances:
    counter += 1  # Increment the counter each time the user makes a guess
    
    # Prompt the user to guess a number and convert the input to an integer
    try:
        myguess = int(input("Guess a number between 0 and 100: "))
    except ValueError:  # Handle the case where the input is not an integer
        print("Please enter a valid number.")
        continue
    
    # Check if the guess is too low, too high, or correct
    if myguess < guess:
        print("The real number is greater than this. Try again!")
    elif myguess > guess:
        print("The real number is lesser than this. Try again!")
    else:
        # User guessed correctly
        print(f"Yay! You got it right in {counter} guesses!")
print("Damn! You lost all chances!")
