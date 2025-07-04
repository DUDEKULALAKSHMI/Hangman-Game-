import random

# Step 1: Define a small list of words
word_list = ["apple", "house", "chair", "robot", "plant"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Step 2: Game setup
guessed_word = ["_"] * word_length
guessed_letters = []
tries = 6

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have", tries, "incorrect guesses allowed.\n")

# Step 3: Game loop
while tries > 0 and "_" in guessed_word:
    print("Word: ", " ".join(guessed_word))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
        print("Correct!\n")
    else:
        tries -= 1
        print(f"Wrong guess! You have {tries} tries left.\n")

# Step 4: End of game
if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print("Sorry, you ran out of tries. The word was:", chosen_word)
