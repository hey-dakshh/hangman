import random

# Predefined word lists
word_lists = {
    "Fruits": ["apple", "banana", "cherry", "date", "elderberry"],
    "Animals": ["lion", "tiger", "bear", "elephant", "giraffe"],
    "Countries": ["usa", "canada", "mexico", "france", "germany"],
    "Food": ["pizza", "sushi", "tacos", "burgers", "fries"]
}

# Ask the player to choose a word type
print("Choose a word type:")
for i, word_type in enumerate(word_lists.keys()):
    print(f"{i+1}. {word_type}")
word_type_choice = int(input("Enter the number of your choice: "))
word_type = list(word_lists.keys())[word_type_choice - 1]

# Select a random word from the chosen list
random_word = random.choice(word_lists[word_type])

# Initialize guessed letters and incorrect guesses
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 5

# Set a hint for the word
hint = f"A type of {word_type.lower()}"

# Set a theme for the game
theme = "Word Wizard"

# Set a difficulty level for the game
difficulty_level = "Easy"

# Set a reward for winning the game
reward = "A virtual trophy"

print(f"Welcome to {theme}! You're playing on {difficulty_level} mode.")
print(f"Your goal is to guess the secret {word_type.lower()} and win {reward}!")

while True:
    # Print the hint
    print(f"Hint: {hint}")

    # Get player guess
    guess = input("Guess a letter: ")

    # Check if the guess is in the word and not already guessed
    if guess in random_word and guess not in guessed_letters:
        guessed_letters.append(guess)
        print("Correct! The word is: ", end="")
        for letter in random_word:
            if letter in guessed_letters:
                print(letter, end="")
            else:
                print("_", end="")
        print()
        print(f"You're getting closer to solving the mystery!")
    elif guess not in random_word and guess not in guessed_letters:
        incorrect_guesses += 1
        print("Incorrect! The word is: ", end="")
        for letter in random_word:
            if letter in guessed_letters:
                print(letter, end="")
            else:
                print("_", end="")
        print()
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
        print("Be careful, you're running out of chances!")
    else:
        print("You already guessed that letter! Try again.")

    # Check if the game is over
    if all(letter in guessed_letters for letter in random_word):
        print("Congratulations! You won!")
        print(f"You guessed the secret {word_type.lower()}: {random_word}")
        print(f"You won {reward}!")
        break
    elif incorrect_guesses >= max_incorrect_guesses:
        print(f"Game over! The secret {word_type.lower()} was {random_word}.")
        print("Better luck next time!")
        break