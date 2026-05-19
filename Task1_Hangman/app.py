import random

words = ["apple", "tiger", "chair", "robot", "plant"]
chosen_word = random.choice(words)

display = ["_"] * len(chosen_word)

print("🎮 Welcome to Hangman!")
print("Word:", " ".join(display))

attempts = 6
guessed_letters = []

while attempts > 0:
    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter!")
        continue

    # Repeated guess check
    if guess in guessed_letters:
        print("ou already guessed that letter!")
        continue

    guessed_letters.append(guess)

    correct = False

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            correct = True

    if not correct:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

    print("Word:", " ".join(display))
    print("Guessed letters:", ", ".join(guessed_letters))

    if "_" not in display:
        print("🎉 You Win!")
        break

if "_" in display:
    print("😢 You Lose! The word was:", chosen_word)
