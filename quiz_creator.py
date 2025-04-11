#initialize main menu function() to display main menu
def main_menu():
    print("\n********** Welcome to Quiz Creator! **********")
    print("1. Create Quiz")
    print("2. Exit and save to file")
    print("**********************************************")


#Initialize list to store questions and answers to append in
question_data = []

#Initialize a while loop to ask for user input until the user choose to exit
while True:
    main_menu()
    choice = int(input("Choice (1 and 2): "))

    if choice == 1:
        question = input("\nEnter question: ")
        
        answer_a = input("Enter option a: ")
        answer_b = input("Enter option b: ")
        answer_c = input("Enter option c: ")
        answer_d = input("Enter option d: ")

#initialize another while loop within the first one to properly print check and store correct answer
    while True:
        correct_answer = input("Enter the correct answer (a,b,c,d): ").lower()
        if correct_answer in ['a', 'b', 'c', 'd']:
            break
        else:
            print("Invalid choice. Please enter a, b, c, or d")

#Store and write user input into a text file format

