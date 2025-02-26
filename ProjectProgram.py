import random #imported module for randint to generate random numbers

#display title function, game description, and user ready check
def display_title():
    print("Guess the Number Game")
    print("This Program randomly generates a number between 1 and 10 that you will have to guess.")
    print("You will have unlimited attempts.")
    ready_check = ""  #initialize ready_check variable

    #while loop that allows user to select if they want to play
    while ready_check != "yes" and ready_check != "no":
        ready_check = input("Type 'yes' to play or 'no' to exit the program: ")
        if ready_check == "no": #ends program if no is entered
            print("Goodbye!")
            return
        elif ready_check == "yes": #calls play_game function if yes is entered
            play_game()
        else: #error handling to let user know input was invalid and only allow yes/no
            print("That is not a valid input")

#function for playing of game
def play_game():
    secret_number = random.randint(1, 10) #generate random number using randint
    user_guess = 0 #initialize user variable

    #while loop that compares value of user_guess to secret_number with feedback
    while user_guess != secret_number:
        user_guess = int(input("Guess a number between 1 and 10: "))
        if user_guess == secret_number: #when correct number is guessed main is called
            print("Congratulations! You guessed the correct number.")
            return main()
        elif user_guess < secret_number: 
            print("Oops! Your guess was too low. Try again.")
            continue
        else:
            print("Oops! Your guess was too high. Try again.")
            continue
    
#main function that calls display_title
def main():
    display_title()
main()
