# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added

import random

def generate_quiz():

    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    answer = num1 + num2
    return num1, num2, answer

def quiz_question(num1, num2):
    print(f'  {num1}\n+ {num2}\n====')
    user_answer = int(input('Enter your answer: '))
    return user_answer

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print('Congratulations! Your answer is correct.')
    else:
        print(f'Incorrect. The correct answer is {correct_answer}.')

def main():
    num1, num2, answer = generate_quiz()
    user_answer = quiz_question(num1, num2)
    check_answer(user_answer, answer)

if __name__ == "__main__":
    main()

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
