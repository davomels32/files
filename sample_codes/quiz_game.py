def quiz_game_cli():
    questions = [
        ("What is the capital of France?","paris"),
        ("2+2=","4"),
        ("Python is a ___? (language/tool)","language"),
    ]
    score = 0
    print("\n=== Quiz Game (CLI) ===")
    for q,a in questions:
        ans = input(q+" ").strip().lower()
        if ans == a:
            score += 1; print("Correct")
        else:
            print("Wrong")
    print(f"Final score: {score}/{len(questions)}")

if __name__ == '__main__':
    quiz_game_cli()
