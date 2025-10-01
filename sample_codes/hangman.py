import random

def hangman_cli():
    words = ['python','hangman','coding','computer','program']
    word = random.choice(words)
    guessed = set()
    wrong = 0
    print("\n=== Hangman (CLI) ===")
    while True:
        display = ' '.join([c if c in guessed else '_' for c in word])
        print(display)
        if all(c in guessed for c in word):
            print("You win!"); break
        letter = input("Guess a letter: ").strip().lower()
        if letter in word:
            guessed.add(letter)
        else:
            wrong += 1; print(f"Wrong: {wrong}")
            if wrong >= 6:
                print("You lost. Word was", word); break

if __name__ == '__main__':
    hangman_cli()
