import random, json, os

WORDS_FILE = 'hangman_words.json'

def load_words():
    if os.path.exists(WORDS_FILE):
        with open(WORDS_FILE,'r') as f:
            return json.load(f)
    return ['python','hangman','coding','computer','program']

def save_words(words):
    with open(WORDS_FILE,'w') as f:
        json.dump(words,f,indent=4)

def hangman_cli():
    words = load_words()
    print('\n=== Hangman (CLI) ===')
    while True:
        print('\nCommands: play | list | add | remove | quit')
        cmd = input('> ').strip().lower()
        if cmd == 'play':
            word = random.choice(words); guessed=set(); wrong=0
            while True:
                display = ' '.join([c if c in guessed else '_' for c in word]); print(display)
                if all(c in guessed for c in word): print('You win!'); break
                letter = input('Guess a letter: ').strip().lower()
                if letter in word: guessed.add(letter)
                else: wrong+=1; print(f'Wrong: {wrong}'); 
                if wrong>=6: print('You lost. Word was',word); break
        elif cmd == 'list':
            for i,w in enumerate(words,1): print(f"{i}. {w}")
        elif cmd == 'add':
            w = input('Word to add: ').strip().lower(); words.append(w); save_words(words); print('Added.')
        elif cmd == 'remove':
            idx = int(input('Number to remove: ')) -1
            if 0<=idx<len(words): words.pop(idx); save_words(words); print('Removed.')
            else: print('Invalid index.')
        elif cmd == 'quit': break
        else: print('Unknown command.')

if __name__ == '__main__':
    hangman_cli()
