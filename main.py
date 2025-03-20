import random

def choose_word():
    
    words = ["python", "hangman", "challenge", "programming", "computer", "algorithm"]
    return random.choice(words)

def hangman():
    word = choose_word()
    attempts = 3  
    hints_given = 0  

    print("Welcome to Hangman!")
    print("Here are the possible words you might need to guess:")
    print(["python", "hangman", "challenge", "programming", "computer", "algorithm"])
    print(f"\nYou have {attempts} attempts to guess the word. Let's begin!")

    while attempts > 0:
        guess = input("\nGuess the word: ").lower()

        if guess == word:
            print(f"Congratulations! You've guessed the word '{word}' correctly!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong guess! You have {attempts} attempts left.")
                
               
                if hints_given == 0:
                    print(f"Hint: The word starts with the letter '{word[0]}'.")
                    hints_given += 1
                elif hints_given == 1:
                    print(f"Hint: The word ends with the letter '{word[-1]}'.")
                    hints_given += 1
            else:
                print(f"Game over! You ran out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    hangman()
