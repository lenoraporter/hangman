import random   # Imports the random module to generate random selections.
from words import word_list  # Imports a list named 'word_list' from a module/file named 'words'.


def get_word():  # Defines a function named 'get_word' to pick a random word.
    word = random.choice(word_list)  # Selects a random word from 'word_list'.
    return word.upper()  # Converts the word to uppercase and returns it.


def play(word):  # Defines the function 'play' that contains the main game logic, accepting 'word' as an argument.
    word_completion = "_" * len(word)  # Creates a string of underscores equal to the length of 'word'.
    guessed = False  # Initializes a boolean to track whether the word has been guessed.
    guessed_letters = []  # Initializes a list to keep track of guessed letters.
    guessed_words = []  # Initializes a list to keep track of guessed words.
    tries = 6  # Sets the number of tries (or lives) the player has.
    print("Let's play Hangman!")  # Prints a welcoming message.
    print(display_hangman(tries))  # Displays the hangman image for the current number of tries.
    print(word_completion)  # Prints the word completion status with underscores.
    print("\n")  # Prints a newline for better readability.

    while not guessed and tries > 0:  # Begins a loop that continues as long as the word isn't guessed and tries remain.
        guess = input("Please guess a letter or word: ").upper()  # Asks for a user input and converts it to uppercase.
        if len(guess) == 1 and guess.isalpha():  # Checks if the guess is a single alphabetic character.
            if guess in guessed_letters:  # Checks if the letter has already been guessed.
                print("You already guessed the letter", guess)  # Informs the player the letter was already guessed.
            elif guess not in word:  # Checks if the guessed letter is not in the word.
                print(guess, "is not in the word.")  # Informs the player the guess was incorrect.
                tries -= 1  # Reduces the number of tries left by one.
                guessed_letters.append(guess)  # Adds the guessed letter to the list of guessed letters.
            else:  # The case where the guess is correct and hasn't been guessed before.
                print("Good job,", guess, "is in the word!")  # Congratulates the player for a correct guess.
                guessed_letters.append(guess)  # Adds the guessed letter to the list of guessed letters.
                word_as_list = list(word_completion)  # Converts the string of word_completion into a list.
                indices = [i for i, letter in enumerate(word) if letter == guess]  # Finds all indices of the guessed letter in the word.
                for index in indices:  # Loops through each index.
                    word_as_list[index] = guess  # Replaces the underscore with the guessed letter in the correct position.
                word_completion = "".join(word_as_list)  # Joins the list back into a string.
                if "_" not in word_completion:  # Checks if there are no more underscores left, meaning the word has been fully guessed.
                    guessed = True  # Sets 'guessed' to True, ending the game.
        elif len(guess) == len(word) and guess.isalpha():  # Checks if the guess is a whole word and is alphabetic.
            if guess in guessed_words:  # Checks if the word has already been guessed.
                print("You already guessed the word", guess)  # Informs the player the word was already guessed.
            elif guess != word:  # Checks if the guessed word is not the correct word.
                print(guess, "is not the word.")  # Informs the player the guess was incorrect.
                tries -= 1  # Reduces the number of tries left by one.
                guessed_words.append(guess)  # Adds the guessed word to the list of guessed words.
            else:  # The case where the guessed word is correct.
                guessed = True  # Sets 'guessed' to True, ending the game.
                word_completion = word  # Sets word_completion to the fully correct word.
        else:  # Handles the case where the guess is neither a single letter nor the correct length word.
            print("Not a valid guess.")  # Informs the player the guess was not valid.

        print(display_hangman(tries))  # Updates and displays the hangman drawing.
        print(word_completion)  # Prints the current status of the word.
        print("\n")  # Adds a newline for better separation.
    if guessed:  # Checks if the word has been successfully guessed.
        print("Congrats, you guessed the word! You win!")  # Congratulates the player on winning.
    else:  # If not guessed and tries are 0.
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")  # Informs the player they have run out of tries and reveals the word.

### Displaying the Hangman State

def display_hangman(tries): # Defines the function 'display_hangman' to show the hangman's state based on remaining tries.
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():  # Defines the main function that orchestrates the game.
    word = get_word()  # Gets a random word to start the game.
    play(word)  # Starts the game using the selected word.
    while input("Play Again? (Y/N) ").upper() == "Y":  # Post-game loop to check if the player wants to play again.
        word = get_word()  # Gets a new word if the player decides to continue playing.
        play(word)  # Starts a new game with the new word.

if __name__ == "__main__":  # Ensures the following block only runs if the script is executed as the main program.
    main()  # Calls the 'main' function to start the game.
