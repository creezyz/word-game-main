import random
with open("words.txt", "r") as file:
    words = [line.strip().lower() for line in file if line.strip()]
    
word= random.choice(words)
guessedWord = ["_"] * len(word)
attempts = 10

while attempts > 0:
    print("Current word: " + " ".join(guessedWord))
    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in guessedWord:
        print("You already guessed that letter.")
        continue
    
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessedWord[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")
    
    if "_" not in guessedWord:
        print("Congratulations! You've guessed the word: " + word)
        break

