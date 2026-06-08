import random
with open("words.txt", "r") as file:
    words = [line.strip().lower() for line in file if line.strip()]
    
word= random.choice(words)
guessedWord = ["_"] * len(word)
attempts = 10


