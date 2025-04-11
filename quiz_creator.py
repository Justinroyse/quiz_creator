#initialize main menu function() to display main menu
def main_menu(quiz_started):
    print("\n********** Welcome to Quiz Creator! **********")

    if not quiz_started:
        print("1. Create Quiz")
    else:
        print("1. Create New Question")

    print("2. Exit and save to file")
    print("**********************************************")


#Initialize list to store questions and answers to append in
question_data = []

#Track if the first question is created so that the main menu option will change
quiz_started = False

#Initialize a while loop to ask for user input until the user choose to exit
while True:
    main_menu(quiz_started)
    choice = int(input("\nChoice (1 or 2): "))

    if choice == 1:
        quiz_started = True

        print("\n--- Creating a New Question ---")
        question = input("\nEnter your quiz question:\n>")
        
        print("\nNow enter the 4 options:")
        answer_a = input("a) ")
        answer_b = input("b) ")
        answer_c = input("c) ")
        answer_d = input("d) ")

#Initialize another while loop within the first one to properly print check and store correct answer
        while True:
            correct_answer = input("\nEnter the correct answer (a,b,c,d): ").lower()
            if correct_answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print("Invalid choice. Please enter a, b, c, or d") 

#store the question and answer entry as a formatted sting to apppend in the question datas
        question_entry = (
            f"Question: {question}\n"
            f"a) {answer_a}\n"
            f"b) {answer_b}\n"
            f"c) {answer_c}\n"
            f"d) {answer_d}\n"
            f"Correct Answer: {correct_answer}\n"
            f"{'-'*30}\n"
        )
        question_data.append(question_entry)

#Store and write user input into a text file format
    elif choice == 2:
        with open("quiz_questions.txt", "w") as file:
            for entry in question_data:
                file.write(entry)
        print("\n--- All questions saved to (quiz_questions.txt) ---")
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1 or 2.")



