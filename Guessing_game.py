# GUESSING GAME
import random

# Generating a random number between 1 and 20, 21 is exclusive.
num = random.randrange(1, 21)
# print(num) # for debugging purpose.

# Taking user input. Input validation is not done so the user must enter only valid numbers in the range 1, 2, 3...20.
q = int(input("Guess the correct number between 1 and 20: "))
flag = False

# Creating the main method.
def main(q, num):
    attempt = 10
    total__attempt = attempt

    while attempt > 0:
        if q > num: # If user input is greater than the actual number, then do the following.
            flag = False
            attempt -= 1
            print("\nAttempts left:", attempt)
            if attempt == 0:
                break
            q = int(input(f"Your guess is greater. Please enter a number smaller than {q}: "))
        elif q < num: # If user input is smaller than the actual number, then do the following.
            flag = False
            attempt -= 1
            print("\nAttempts left:", attempt)
            if attempt == 0:
                break
            q = int(input(f"Your guess is smaller. Please enter a number greater than {q}: "))  
        else: # If the user input is equal to the actual number, then do the following.
            flag = True
            print("Congratulations.. You won")
            print("Attempts made:", total__attempt + 1 - attempt)
            break
    
    if flag == False: # If total attempt left is equal to zero, then this line of code is executed.
        print("You lose")


main(q, num)

