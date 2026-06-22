import random
words = ["apple", "python", "cat", "book", "code"]
word = random.choice(words)
guessed = ""
print("Welcome to Hangman")
while True:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    print(display)
    if "_" not in display:
        print("You Won!")
        break
    guess = input("Enter a letter: ").lower()
    guessed += guess