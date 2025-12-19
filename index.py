import random

name = input("Enter your name: ")
print("Welcome", name, "🙂")

words = ["add", "multi", "code", "structure"]
word = random.choice(words)

correct = ""
chance = 6

# Hangman drawings (stage by stage)
hangman = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

print("\nGuess the word!\n")

while chance > 0:

    show = ""

    for letter in word:
        if letter in correct:
            show += letter + " "
        else:
            show += "_ "

    print(show)
    print(hangman[6 - chance])   # drawing show

    if "_" not in show:
        print("\n🎉 You Win!")
        print("The word is:", word)
        break

    guess = input("Guess one letter: ")
    correct += guess

    if guess not in word:
        chance -= 1
        print("❌ Wrong! Chances left:", chance)

if chance == 0:
    print(hangman[6])
    print("\n💔 You Lose!")
    print("The word was:", word)
