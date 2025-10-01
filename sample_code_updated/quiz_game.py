import json, os

DATA_FILE = 'quiz.json'

def load_quiz():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,'r') as f:
            return json.load(f)
    return [
        {'q':'What is the capital of France?','a':'paris'},
        {'q':'2+2=','a':'4'}
    ]

def save_quiz(qs):
    with open(DATA_FILE,'w') as f:
        json.dump(qs,f,indent=4)

def quiz_game_cli():
    qs = load_quiz()
    print('\n=== Quiz Game (CLI) ===')
    while True:
        print('\nCommands: play | list | add | edit | delete | quit')
        cmd = input('> ').strip().lower()
        if cmd == 'play':
            score=0
            for item in qs:
                ans = input(item['q']+' ').strip().lower()
                if ans==item['a']: score+=1; print('Correct')
                else: print('Wrong')
            print(f'Final score: {score}/{len(qs)}')
        elif cmd == 'list':
            for i,item in enumerate(qs,1): print(f"{i}. Q: {item['q']} A: {item['a']}")
        elif cmd == 'add':
            q = input('Question: ').strip(); a = input('Answer: ').strip().lower(); qs.append({'q':q,'a':a}); save_quiz(qs); print('Added.')
        elif cmd == 'edit':
            idx = int(input('Question number to edit: ')) -1
            if 0<=idx<len(qs):
                item = qs[idx]
                nq = input(f"Q [{item['q']}]: ").strip() or item['q']
                na = input(f"A [{item['a']}]: ").strip().lower() or item['a']
                qs[idx] = {'q':nq,'a':na}; save_quiz(qs); print('Updated.')
            else: print('Invalid index.')
        elif cmd == 'delete':
            idx = int(input('Number to delete: ')) -1
            if 0<=idx<len(qs): qs.pop(idx); save_quiz(qs); print('Deleted.')
            else: print('Invalid index.')
        elif cmd == 'quit': break
        else: print('Unknown command.')

if __name__ == '__main__':
    quiz_game_cli()
