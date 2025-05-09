# Import module (random) to load the questions randomly for the user to answer
import random

# Create user defined function for loading the quiz file
def reader(filename):
    with open(filename, "r") as file:
        content = file.read()

    questions_raw = content.strip().split('-' * 40 + '\n')
    questions = []

    for q_raw in questions_raw:
        lines = q_raw.strip().split('\n')
        if len(lines) < 6:
            continue

        question = lines[0].replace("Question: ", " ")
        a = lines[1].replace("a) ", " ")
        b = lines[2].replace("b) ", " ")
        c = lines[3].replace("c) ", " ")
        d = lines[4].replace("d) ", " ")
        correct = lines[5].replace("Correct Answer: ", " ").strip()

        questions.append({
            'question': question,
            'options': {'a': a, 'b': b, 'c': c, 'd': d},
            'correct': correct
        })

    return questions

# Create user defined function for quiz game
def quiz_game(questions):
    score = 0
    asked_questions = []

# Initialize while loop to keep asking for questions until user quits the game
    while True:
        remaining = [question for question in questions if question not in asked_questions]
        if not remaining:
            print("\n You've answered all available questions!")
            break

        question = random.choice(remaining)
        asked_questions.append(question)

        print("\n" + "=" * 50)
        print(f"Question: {question['question']}")
        for key in ['a', 'b', 'c', 'd']:
            print(f"{key}) {question['options'][key]}")

# Acquire user's answer
        while True:
            answer = input("Your answer (a, b, c, d): ").lower()
            if answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print("⚠️ Invalid choice. Please enter a, b, c, or d.")

# Check if the answer is correct
        if answer == question['correct']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question['correct']}) {question['options'][question['correct']]}")

# Ask the user if they want to continue
        continuation = input("\nDo you want to continue? (y/n): ").lower()
        if continuation != "y":
            break

# Displays the final score if the quiz is over and exits the program
    print("\n" + "=" * 50)
    print(f"🏁 Quiz finished! Your final score: {score}/{len(asked_questions)}")
    print("Thanks for playing!")

# Initialize the file to load
if __name__ == "__main__":
    try:
        quiz_questions = reader("quiz_questions.txt")
        if not quiz_questions:
            print("⚠️ No questions found in the quiz file.")
        else:
            quiz_game(quiz_questions)
    except FileNotFoundError:
        print("⚠️ 'quiz_questions.txt' not found. Please run the Quiz Creator first.")

# Finished the prototype program, pending tkinter improved version and add GUI