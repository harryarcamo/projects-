import random

# List of words to guess
words = ['banana', 'elephant', 'sunshine', 'mountain', 'keyboard', 'ocean', 'butterfly', 'coffee', 'guitar', 'candle']

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]  # Create a list of underscores
attempts = 8  # Number of allowed attempts

print("Welcome to Hangman! Beware!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # Reveal the letter
    else:
        print("That letter doesn't appear in the word. NO pressure what so ever")
        attempts -= 1

# Game conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived... for now!")
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost! HAHAHAHAHAHA")
