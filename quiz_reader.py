# Import tkinter
# Import module (random) to load the questions randomly for the user to answer
import tkinter as tk
from tkinter import messagebox
import random

# Create user defined function for loading the quiz file
def reader(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        messagebox.showerror("File Error", f"(Cannot find {filename}")
        return []

    blocks = content.strip().split("-" * 30 + "\n")
    questions = []

    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) < 6:
            continue

        question_text = lines[0].replace("Question: ", "")
        options = {
            'a': lines[1][3:],
            'b': lines[2][3:],
            'c': lines[3][3:],
            'd': lines[4][3:]
        }
        correct = lines[5].replace("Correct Answer: ", "").strip()

        questions.append({
            "question": question_text,
            "options": options,
            "correct": correct
        })

    return questions

# Create quiz class and slowly incorporate it in the prototype quiz game function
class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.master.title("Quiz Game")
        self.questions = random.sample(questions, len(questions))  # Shuffle
        self.index = 0
        self.score = 0
        
        self.question_label = tk.Label(master, text="", font=('Arial', 14), wraplength=500, justify="left")
        self.question_label.pack(pady=20)

        self.buttons = {}
        for key in ['a', 'b', 'c', 'd']:
            btn = tk.Button(master, text="", width=40, font=('Arial', 12),
                            command=lambda opt=key: self.check_answer(opt))
            btn.pack(pady=5)
            self.buttons[key] = btn

        self.feedback = tk.Label(master, text="", font=('Arial', 12, 'italic'))
        self.feedback.pack(pady=10)

        self.next_btn = tk.Button(master, text="Next", font=('Arial', 12), command=self.next_question, state="disabled")
        self.next_btn.pack(pady=10)

        self.score_label = tk.Label(master, text="Score: 0", font=('Arial', 12))
        self.score_label.pack(pady=5)

        self.show_question()

    def show_question(self):
        if self.index >= len(self.questions):
            messagebox.showinfo("Quiz Complete", f"Your score: {self.score}/{len(self.questions)}")
            self.master.quit()
            return

        question = self.questions[self.index]
        self.question_label.config(text=f"Q{self.index+1}: {question['question']}")
        for key in self.buttons:
            self.buttons[key].config(text=f"{key}) {question['options'][key]}", state="normal")

        self.feedback.config(text="")
        self.next_btn.config(state="disabled")
    

    def check_answer(self, selected):
        correct = self.questions[self.index]['correct']
        for key in self.buttons:
            self.buttons[key].config(state="disabled")

        if selected == correct:
            self.feedback.config(text="✅ Correct!", fg="green")
            self.score += 1
        else:
            correct_text = self.questions[self.index]['options'][correct]
            self.feedback.config(text=f"❌ Wrong! Correct: {correct}) {correct_text}", fg="red")

        self.score_label.config(text=f"Score: {self.score}")
        self.next_btn.config(state="normal")

    def next_question(self):
        self.index += 1
        self.show_question()

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