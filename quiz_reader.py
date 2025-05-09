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
    

