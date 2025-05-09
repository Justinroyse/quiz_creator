# Import tkinter
# Import module (random) to load the questions randomly for the user to answer
import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

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
        
        self.bg_image = Image.open("background_image.jpg")  # Use your image path
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self.master, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.clear_window()

        self.welcome_label = tk.Label(self.master, text="Welcome to the Quiz Game!", font=("Arial", 18))
        self.welcome_label.pack(pady=30)

        self.start_button = tk.Button(self.master, text="Start Quiz", font=("Arial", 14), command=self.start_quiz)
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(self.master, text="Quit", font=("Arial", 14), command=self.master.quit)
        self.quit_button.pack(pady=10)

    def start_quiz(self):
        self.clear_window()
        self.build_quiz_ui()
        self.show_question()

    def build_quiz_ui(self):
        self.question_label = tk.Label(self.master, text="", font=('Arial', 14), wraplength=500, justify="left")
        self.question_label.pack(pady=20)

        self.buttons = {}
        for key in ['a', 'b', 'c', 'd']:
            btn = tk.Button(self.master, text="", width=40, font=('Arial', 12),
                            command=lambda opt=key: self.check_answer(opt))
            btn.pack(pady=5)
            self.buttons[key] = btn

        self.feedback = tk.Label(self.master, text="", font=('Arial', 12, 'italic'))
        self.feedback.pack(pady=10)

        self.next_btn = tk.Button(self.master, text="Next", font=('Arial', 12), command=self.next_question, state="disabled")
        self.next_btn.pack(pady=10)

        self.quit_btn = tk.Button(self.master, text="Quit", font=('Arial', 12), command=self.master.quit)
        self.quit_btn.pack(pady=5)

        self.score_label = tk.Label(self.master, text="Score: 0", font=('Arial', 12))
        self.score_label.pack(pady=5)

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

    def clear_window(self):
        for widget in self.master.winfo_children():
            if widget != self.bg_label:
                widget.destroy()

# Initialize the file to load
if __name__ == "__main__":
    questions = reader("quiz_questions.txt")
    if questions:
        root = tk.Tk()
        root.title("Quiz Game")
        app = QuizApp(root, questions)
        root.mainloop()

# Finished Third Working Protoype Program