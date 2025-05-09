# Import module (random) to load the questions randomly for the user to answer
import random

# Create user defined function for loading the quiz file
def reader(filename):
    with open(filename, "r") as file:
        content = file.read()

    questions_raw = content.strip().split('-' * 40 + '\n')
    questions = []

# Create user defined function for quiz game

