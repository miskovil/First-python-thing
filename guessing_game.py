
secWord = input("Please designate the secret word: ").lower()
# word we are looking for
guess = ""
# courent guess
guess_count = 0
# how many times the player guesses

guess_limit = int(input("Please designate the maximum number of guesses: "))
# the limit of guesses

out_of_guesses = False
# is the player out of guesses

if guess_limit <= 0:
    print("You entered a number that is not supported! The game will now end.")


while guess.lower() != secWord and not(out_of_guesses):
    # Continues until you are either out of guesses or guessed correctly
    if guess_count < guess_limit:
    # Checks if you got guesses remaining
        guess = input("Enter guess ")
        # Asks for a input and stores the answer under the variable guess
        guess_count += 1
        # Adds one to the guess count
        if secWord != guess:
            print("You have " + str(guess_limit - guess_count) + " guesses left")
        # If you guessed incorrectly prints out how many guesses you have left
        else:
            print("")
            # If you guessed correctly prints nothing
    else:
        out_of_guesses = True
        # Ends while loop because you are out of guesses

if out_of_guesses:
    print("You loose!")
    # If the boolean Out_of_guesses is true prints out loss message
else:
    print("You win! \nYou won with " + str(guess_limit - guess_count) + " guesses left!")
    # Otherwise prints out a win message alongside the number of guesses you had left

