import random 

def display_title():
    print("Guess the Number Game")
    print("This Program randomly generates a number between 1 and 10 that you will have to guess.")
    print("You will have unlimited attempts.")
    ready_check = ""  
    
    while ready_check != "yes" and ready_check != "no":
        ready_check = input("Type 'yes' to play or 'no' to exit the program: ")
        if ready_check == "no": 
            print("Goodbye!")
            return
        elif ready_check == "yes": 
            play_game()
        else: 
            print("That is not a valid input")
"""
Function starts by printing game title and description.

ready_check variable is initialized and then used to determine if 
user is ready to play by accepting yes/no input.

while loop compares ready_check input and closes if no, calls play_game function 
if yes and for everything else returns an error statement.
"""


def play_game():
    secret_number = random.randint(1, 10) 
    user_guess = 0 

    while user_guess != secret_number:
        user_guess = int(input("Guess a number between 1 and 10: "))
        if user_guess == secret_number: 
            print("Congratulations! You guessed the correct number.")
            return main()
        elif user_guess < secret_number: 
            print("Oops! Your guess was too low. Try again.")
            continue
        else:
            print("Oops! Your guess was too high. Try again.")
            continue
"""
secret_number uses randint method to generate a random number and user_guess initialized.

while loop compares value of user_guess and secret_number after user inputs their guess.
If correct, main() is called to start the game again. 
Feedback given for guesses to high and too low.
"""
    
def main():
    display_title()
main()
